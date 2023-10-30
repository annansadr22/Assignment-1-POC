import grpc
import inventory_pb2
import inventory_pb2_grpc
import time
import numpy as np

array=np.zeros((5, 100))
i=0
j=0
k=0
l=0
m=0

def search_by_id(stub):
    global i
    request = inventory_pb2.InventoryRecord(inventory_id='IN0050')
    start_time = time.time()
    response = stub.SearchByID(request)
    end_time = time.time()
    if response.inventory_id:
        print(f"Found record: {response.name} ({response.inventory_id})")
    else:
        print("Record not found")
    print(f"Response time for Search by ID: {end_time - start_time} seconds")


    array[0][i]=end_time - start_time
    i+=1





def search_by_key_value(stub):
    global j
    request = inventory_pb2.SearchReq(key_name='quantity_in_reorder', key_value='50')
    start_time = time.time()
    response = stub.Search(request)
    end_time = time.time()
    if (response.inventory_record.inventory_id or
            response.inventory_record.name or
            response.inventory_record.description or
            response.inventory_record.unit_price or
            response.inventory_record.quantity_in_stock or
            response.inventory_record.inventory_value or
            response.inventory_record.reorder_level or
            response.inventory_record.reorder_time_in_days or
            response.inventory_record.quantity_in_reorder or
            response.inventory_record.discontinued):
        print(f"Found record: {response.inventory_record.name} ({response.inventory_record.inventory_id})")
    else:
        print("Record not found")
    print(f"Response time for Search by Key Value: {end_time - start_time} seconds")

    array[1][j] = end_time - start_time
    j += 1

def search_by_key_range(stub):
    global k
    request = inventory_pb2.RangeReq(key_name='reorder_time_in_days', key_start=0, key_end=5)
    start_time = time.time()
    response = stub.SearchRange(request)
    end_time = time.time()
    if response.inventory_record:
        for record in response.inventory_record:
            print(f"Found record: {record.name} ({record.inventory_id})")
    else:
        print("No records found")
    print(f"Response time for Search by Key Range: {end_time - start_time} seconds")

    array[2][k] = end_time - start_time
    k += 1

def get_distribution(stub):
    global l
    request = inventory_pb2.DistReq(key_name='quantity_in_reorder', percentile=0.5)
    start_time = time.time()
    response = stub.GetDistribution(request)
    end_time = time.time()
    if response.inventory_record:
        for record in response.inventory_record:
            print(f"Found record: {record.name} ({record.inventory_id})")
    else:
        print("No records found")
    print(f"Response time for Get Distribution: {end_time - start_time} seconds")

    array[3][l] = end_time - start_time
    l += 1

def update_record(stub):
    global m
    key_name = "inventory_id"
    key_value = "IN0001"
    val_name = "quantity_in_reorder"
    val_value_new = "60"
    start_time = time.time()
    response = stub.Update(inventory_pb2.UpdateReq(
        key_name=key_name,
        key_value=key_value,
        val_name=val_name,
        val_value_new=val_value_new
    ))
    end_time = time.time()
    if response:
        print(f"Record updated successfully: {response.name}")
    else:
        print("Record not found or update failed")
    print(f"Response time for Update Record: {end_time - start_time} seconds")

    array[4][m] = end_time - start_time
    m += 1

def run():
    channel = grpc.insecure_channel('54.82.120.24:50051')
    stub = inventory_pb2_grpc.InventoryStub(channel)

    while True:
        print("Select an option:")
        print("1. Search by ID")
        print("2. Search by Key Value")
        print("3. Search by Key Range")
        print("4. Get Distribution")
        print("5. Update Record")
        print("6. Time Array")
        print("0. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            search_by_id(stub)
        elif choice == "2":
            search_by_key_value(stub)
        elif choice == "3":
            search_by_key_range(stub)
        elif choice == "4":
            get_distribution(stub)
        elif choice == "5":
            update_record(stub)
        elif choice == "6":
            print(array)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    run()
