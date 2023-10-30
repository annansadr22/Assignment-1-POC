import grpc
from concurrent import futures
import inventory_pb2
import inventory_pb2_grpc
import pandas as pd  # Import pandas
import numpy as np

class InventoryServicer(inventory_pb2_grpc.InventoryServicer):
    def __init__(self):
        # Initialize an in-memory data structure for the inventory by loading data from XLSX
        self.inventory_data = self.load_inventory_data()

    def load_inventory_data(self):
        # Load data from the XLSX file into a pandas DataFrame
        df = pd.read_excel('inventory.xlsx')
        print(df)
        # row_data = df.loc[1]
        # print(row_data)


        # Convert the DataFrame into a dictionary of InventoryRecord messages
        inventory_data = {}
        for index, row in df.iterrows():
            inventory_record = inventory_pb2.InventoryRecord(
                inventory_id=str(row['Inventory ID']),
                name=str(row['Name']),
                description=str(row['Description']),
                unit_price=int(row['Unit Price']),
                quantity_in_stock=int(row['Quantity in Stock']),
                inventory_value=int(row['Inventory Value']),
                reorder_level=int(row['Reorder Level']),
                reorder_time_in_days=int(row['Reorder Time in Days']),
                quantity_in_reorder=int(row['Quantity in Reorder']),
                discontinued=row['Discontinued?']
            )
            inventory_data[row['Inventory ID']] = inventory_record


        return inventory_data
    # ...

# Rest of your server code remains the same

    def SearchByID(self, request, context):
        # Implement the logic to search by ID here
        inventory_id = request.inventory_id
        if inventory_id in self.inventory_data:
            return self.inventory_data[inventory_id]
        else:
            return inventory_pb2.InventoryRecord()  # Return an empty record if not found

    # Implement other service methods similarly
    def Search(self, request, context):
        key_name = request.key_name
        key_value = request.key_value
        for inventory_record in self.inventory_data.values():
            key=inventory_record.inventory_id
            if key_name == 'inventory_id' and inventory_record.inventory_id== key_value:
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])
            elif key_name == 'name' and inventory_record.name == key_value:
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'description' and inventory_record.description == key_value:
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'unit_price' and inventory_record.unit_price == int(key_value):
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'quantity_in_stock' and inventory_record.quantity_in_stock == int(key_value):
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'inventory_value' and inventory_record.inventory_value == int(key_value):
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'reorder_level' and inventory_record.reorder_level == int(key_value):
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'reorder_time_in_days' and inventory_record.reorder_time_in_days == int(key_value):
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'quantity_in_reorder' and inventory_record.quantity_in_reorder == int(key_value):
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])

            elif key_name == 'discontinued' and inventory_record.discontinued == key_value:
                return inventory_pb2.SearchRes(inventory_record=self.inventory_data[key])
        else:
            return inventory_pb2.SearchRes()

    def SearchRange(self, request, context):
        key_name = request.key_name
        key_start = request.key_start
        key_end = request.key_end

        matching_records = []
        for inventory_record in self.inventory_data.values():
            key_value = getattr(inventory_record, key_name)

            if key_start <= key_value <= key_end:
                matching_records.append(inventory_record)

        return inventory_pb2.RangeRes(inventory_record=matching_records)

    def GetDistribution(self, request, context):
        key_name = request.key_name
        percentile = request.percentile

        # Create an empty list to store the values for the given key_name
        values = []
        for inventory_record in self.inventory_data.values():
            value=getattr(inventory_record, key_name)
            values.append(value)

        if values:
            # Ensure values list is not empty
            percentile_value = np.percentile(values, percentile * 100)
        response = inventory_pb2.DistRes()

        if percentile_value is not None:
            response.inventory_record.append(
                inventory_pb2.InventoryRecord(name=f"Percentile {percentile * 100}", inventory_id=str(percentile_value))
            )

        return response

    def Update(self, request, context):
        key_name = request.key_name
        key_value = request.key_value
        val_name = request.val_name
        val_value_new = int(request.val_value_new)

        for inventory_record in self.inventory_data.values():
            if key_name == 'inventory_id' and key_value == inventory_record.inventory_id:
                setattr(inventory_record,val_name,val_value_new)
                return inventory_record

        # Implement the logic to update the record based on the provided parameters
        # if key_name in self.inventory_data and hasattr(self.inventory_data[key_name], key_value):
        #     # Check if the key exists and the attribute name is valid
        #     setattr(self.inventory_data[key_name], val_name, val_value_new)
        #     return self.inventory_data[key_name,]  # Return the updated record
        # else:
        return inventory_pb2.InventoryRecord()  # Return an empty record if not found


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServicer_to_server(InventoryServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
