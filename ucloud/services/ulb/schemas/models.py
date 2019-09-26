""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class BackendSetSchema(schema.ResponseSchema):
    """ BackendSet - ulb添加rs时返回的信息
    """

    fields = {
        "BackendId": fields.Str(required=True, load_from="BackendId"),
        "ResourceId": fields.Str(required=True, load_from="ResourceId"),
    }


class ULBSSLSetSchema(schema.ResponseSchema):
    """ ULBSSLSet - DescribeULB
    """

    fields = {
        "HashValue": fields.Str(required=False, load_from="HashValue"),
        "SSLId": fields.Str(required=False, load_from="SSLId"),
        "SSLName": fields.Str(required=False, load_from="SSLName"),
    }


class PolicyBackendSetSchema(schema.ResponseSchema):
    """ PolicyBackendSet - 内容转发下rs详细信息
    """

    fields = {
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "ObjectId": fields.Str(required=False, load_from="ObjectId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
    }


class ULBBackendSetSchema(schema.ResponseSchema):
    """ ULBBackendSet - DescribeULB
    """

    fields = {
        "BackendId": fields.Str(required=False, load_from="BackendId"),
        "Enabled": fields.Int(required=False, load_from="Enabled"),
        "Port": fields.Int(required=False, load_from="Port"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "Status": fields.Int(required=False, load_from="Status"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=False, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Str(
            required=False, load_from="SubResourceType"
        ),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Weight": fields.Int(required=False, load_from="Weight"),
    }


class ULBIPSetSchema(schema.ResponseSchema):
    """ ULBIPSet - DescribeULB
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "EIP": fields.Str(required=False, load_from="EIP"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
    }


class ULBVServerSetSchema(schema.ResponseSchema):
    """ ULBVServerSet - DescribeULB
    """

    fields = {
        "BackendSet": fields.List(ULBBackendSetSchema()),
        "ClientTimeout": fields.Int(required=False, load_from="ClientTimeout"),
        "Domain": fields.Str(required=True, load_from="Domain"),
        "FrontendPort": fields.Int(required=False, load_from="FrontendPort"),
        "ListenType": fields.Str(required=False, load_from="ListenType"),
        "Method": fields.Str(required=False, load_from="Method"),
        "MonitorType": fields.Str(required=True, load_from="MonitorType"),
        "Path": fields.Str(required=True, load_from="Path"),
        "PersistenceInfo": fields.Str(
            required=False, load_from="PersistenceInfo"
        ),
        "PersistenceType": fields.Str(
            required=False, load_from="PersistenceType"
        ),
        "PolicySet": fields.List(ULBPolicySetSchema()),
        "Protocol": fields.Str(required=False, load_from="Protocol"),
        "SSLSet": fields.List(ULBSSLSetSchema()),
        "Status": fields.Int(required=False, load_from="Status"),
        "VServerId": fields.Str(required=False, load_from="VServerId"),
        "VServerName": fields.Str(required=False, load_from="VServerName"),
    }


class ULBSetSchema(schema.ResponseSchema):
    """ ULBSet - DescribeULB
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "BusinessId": fields.Str(required=False, load_from="BusinessId"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "IPSet": fields.List(ULBIPSetSchema()),
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Resource": fields.List(fields.Str()),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "ULBId": fields.Str(required=False, load_from="ULBId"),
        "ULBName": fields.Str(required=False, load_from="ULBName"),
        "ULBType": fields.Str(required=False, load_from="ULBType"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VServerSet": fields.List(ULBVServerSetSchema()),
    }
