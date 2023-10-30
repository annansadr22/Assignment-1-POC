# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inventory_pb2 as inventory__pb2


class InventoryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchByID = channel.unary_unary(
                '/inventory.Inventory/SearchByID',
                request_serializer=inventory__pb2.InventoryRecord.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRecord.FromString,
                )
        self.Search = channel.unary_unary(
                '/inventory.Inventory/Search',
                request_serializer=inventory__pb2.SearchReq.SerializeToString,
                response_deserializer=inventory__pb2.SearchRes.FromString,
                )
        self.SearchRange = channel.unary_unary(
                '/inventory.Inventory/SearchRange',
                request_serializer=inventory__pb2.RangeReq.SerializeToString,
                response_deserializer=inventory__pb2.RangeRes.FromString,
                )
        self.GetDistribution = channel.unary_unary(
                '/inventory.Inventory/GetDistribution',
                request_serializer=inventory__pb2.DistReq.SerializeToString,
                response_deserializer=inventory__pb2.DistRes.FromString,
                )
        self.Update = channel.unary_unary(
                '/inventory.Inventory/Update',
                request_serializer=inventory__pb2.UpdateReq.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRecord.FromString,
                )


class InventoryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchByID(self, request, context):
        """Service method to search by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Service method to search based on key and value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchRange(self, request, context):
        """Service method to search based on key, start, and end values
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDistribution(self, request, context):
        """Service method to get the distribution percentile for a given key
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Service method to update a record
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchByID': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByID,
                    request_deserializer=inventory__pb2.InventoryRecord.FromString,
                    response_serializer=inventory__pb2.InventoryRecord.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=inventory__pb2.SearchReq.FromString,
                    response_serializer=inventory__pb2.SearchRes.SerializeToString,
            ),
            'SearchRange': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchRange,
                    request_deserializer=inventory__pb2.RangeReq.FromString,
                    response_serializer=inventory__pb2.RangeRes.SerializeToString,
            ),
            'GetDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDistribution,
                    request_deserializer=inventory__pb2.DistReq.FromString,
                    response_serializer=inventory__pb2.DistRes.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=inventory__pb2.UpdateReq.FromString,
                    response_serializer=inventory__pb2.InventoryRecord.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inventory.Inventory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Inventory(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.Inventory/SearchByID',
            inventory__pb2.InventoryRecord.SerializeToString,
            inventory__pb2.InventoryRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.Inventory/Search',
            inventory__pb2.SearchReq.SerializeToString,
            inventory__pb2.SearchRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.Inventory/SearchRange',
            inventory__pb2.RangeReq.SerializeToString,
            inventory__pb2.RangeRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDistribution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.Inventory/GetDistribution',
            inventory__pb2.DistReq.SerializeToString,
            inventory__pb2.DistRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inventory.Inventory/Update',
            inventory__pb2.UpdateReq.SerializeToString,
            inventory__pb2.InventoryRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
