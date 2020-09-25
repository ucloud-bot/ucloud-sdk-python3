""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class RemoteVPNGatewayDataSetSchema(schema.ResponseSchema):
    """RemoteVPNGatewayDataSet - DescribeRemoteVPNGateway返回参数"""

    fields = {
        "ActiveTunnels": fields.Str(required=False, load_from="ActiveTunnels"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RemoteVPNGatewayAddr": fields.Str(
            required=False, load_from="RemoteVPNGatewayAddr"
        ),
        "RemoteVPNGatewayId": fields.Str(
            required=False, load_from="RemoteVPNGatewayId"
        ),
        "RemoteVPNGatewayName": fields.Str(
            required=False, load_from="RemoteVPNGatewayName"
        ),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "TunnelCount": fields.Int(required=False, load_from="TunnelCount"),
    }


class IPSecDataSchema(schema.ResponseSchema):
    """IPSecData - IPSec参数"""

    fields = {
        "IPSecAuthenticationAlgorithm": fields.Str(
            required=False, load_from="IPSecAuthenticationAlgorithm"
        ),
        "IPSecEncryptionAlgorithm": fields.Str(
            required=False, load_from="IPSecEncryptionAlgorithm"
        ),
        "IPSecLocalSubnetIds": fields.List(fields.Str()),
        "IPSecPFSDhGroup": fields.Str(
            required=False, load_from="IPSecPFSDhGroup"
        ),
        "IPSecProtocol": fields.Str(required=False, load_from="IPSecProtocol"),
        "IPSecRemoteSubnets": fields.List(fields.Str()),
        "IPSecSALifetime": fields.Str(
            required=False, load_from="IPSecSALifetime"
        ),
        "IPSecSALifetimeBytes": fields.Str(
            required=False, load_from="IPSecSALifetimeBytes"
        ),
    }


class IKEDataSchema(schema.ResponseSchema):
    """IKEData - IKE信息"""

    fields = {
        "IKEAuthenticationAlgorithm": fields.Str(
            required=False, load_from="IKEAuthenticationAlgorithm"
        ),
        "IKEDhGroup": fields.Str(required=False, load_from="IKEDhGroup"),
        "IKEEncryptionAlgorithm": fields.Str(
            required=False, load_from="IKEEncryptionAlgorithm"
        ),
        "IKEExchangeMode": fields.Str(
            required=False, load_from="IKEExchangeMode"
        ),
        "IKELocalId": fields.Str(required=False, load_from="IKELocalId"),
        "IKEPreSharedKey": fields.Str(
            required=False, load_from="IKEPreSharedKey"
        ),
        "IKERemoteId": fields.Str(required=False, load_from="IKERemoteId"),
        "IKESALifetime": fields.Str(required=False, load_from="IKESALifetime"),
        "IKEVersion": fields.Str(required=False, load_from="IKEVersion"),
    }


class VPNTunnelDataSetSchema(schema.ResponseSchema):
    """VPNTunnelDataSet - DescribeVPNTunnel信息"""

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "IKEData": IKEDataSchema(),
        "IPSecData": IPSecDataSchema(),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RemoteVPNGatewayId": fields.Str(
            required=False, load_from="RemoteVPNGatewayId"
        ),
        "RemoteVPNGatewayName": fields.Str(
            required=False, load_from="RemoteVPNGatewayName"
        ),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "VPNGatewayId": fields.Str(required=False, load_from="VPNGatewayId"),
        "VPNGatewayName": fields.Str(
            required=False, load_from="VPNGatewayName"
        ),
        "VPNTunnelId": fields.Str(required=False, load_from="VPNTunnelId"),
        "VPNTunnelName": fields.Str(required=False, load_from="VPNTunnelName"),
    }
