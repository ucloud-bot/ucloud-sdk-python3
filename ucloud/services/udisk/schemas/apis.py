""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.udisk.schemas import models


""" UDisk API Schema
"""


"""
API: AttachUDisk

将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作
"""


class AttachUDiskRequestSchema(schema.RequestSchema):
    """AttachUDisk - 将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作"""

    fields = {
        "MultiAttach": fields.Str(required=False, dump_to="MultiAttach"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class AttachUDiskResponseSchema(schema.ResponseSchema):
    """AttachUDisk - 将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作"""

    fields = {
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
    }


"""
API: CloneUDisk

从UDisk创建UDisk克隆
"""


class CloneUDiskRequestSchema(schema.RequestSchema):
    """CloneUDisk - 从UDisk创建UDisk克隆"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Comment": fields.Str(required=False, dump_to="Comment"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SourceId": fields.Str(required=True, dump_to="SourceId"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CloneUDiskResponseSchema(schema.ResponseSchema):
    """CloneUDisk - 从UDisk创建UDisk克隆"""

    fields = {
        "UDiskId": fields.List(
            fields.Str(), required=False, load_from="UDiskId"
        )
    }


"""
API: CloneUDiskSnapshot

从快照创建UDisk克隆
"""


class CloneUDiskSnapshotRequestSchema(schema.RequestSchema):
    """CloneUDiskSnapshot - 从快照创建UDisk克隆"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Comment": fields.Str(required=False, dump_to="Comment"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SourceId": fields.Str(required=True, dump_to="SourceId"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CloneUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """CloneUDiskSnapshot - 从快照创建UDisk克隆"""

    fields = {
        "UDiskId": fields.List(
            fields.Str(), required=False, load_from="UDiskId"
        )
    }


"""
API: CreateUDisk

创建UDisk磁盘
"""


class CreateUDiskRequestSchema(schema.RequestSchema):
    """CreateUDisk - 创建UDisk磁盘"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "CmkId": fields.Str(required=False, dump_to="CmkId"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "UKmsMode": fields.Str(required=False, dump_to="UKmsMode"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUDiskResponseSchema(schema.ResponseSchema):
    """CreateUDisk - 创建UDisk磁盘"""

    fields = {
        "UDiskId": fields.List(
            fields.Str(), required=False, load_from="UDiskId"
        )
    }


"""
API: CreateUDiskSnapshot

创建snapshot快照
"""


class CreateUDiskSnapshotRequestSchema(schema.RequestSchema):
    """CreateUDiskSnapshot - 创建snapshot快照"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "Comment": fields.Str(required=False, dump_to="Comment"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class CreateUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """CreateUDiskSnapshot - 创建snapshot快照"""

    fields = {
        "SnapshotId": fields.List(
            fields.Str(), required=True, load_from="SnapshotId"
        )
    }


"""
API: DeleteUDisk

删除UDisk
"""


class DeleteUDiskRequestSchema(schema.RequestSchema):
    """DeleteUDisk - 删除UDisk"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DeleteUDiskResponseSchema(schema.ResponseSchema):
    """DeleteUDisk - 删除UDisk"""

    fields = {}


"""
API: DeleteUDiskSnapshot

删除Snapshot
"""


class DeleteUDiskSnapshotRequestSchema(schema.RequestSchema):
    """DeleteUDiskSnapshot - 删除Snapshot"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SnapshotId": fields.Str(required=False, dump_to="SnapshotId"),
        "UDiskId": fields.Str(required=False, dump_to="UDiskId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DeleteUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """DeleteUDiskSnapshot - 删除Snapshot"""

    fields = {}


"""
API: DescribeUDisk

获取UDisk实例
"""


class DescribeUDiskRequestSchema(schema.RequestSchema):
    """DescribeUDisk - 获取UDisk实例"""

    fields = {
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "IsBoot": fields.Str(required=False, dump_to="IsBoot"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ProtocolVersion": fields.Int(
            required=False, dump_to="ProtocolVersion"
        ),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UDiskId": fields.Str(required=False, dump_to="UDiskId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUDiskResponseSchema(schema.ResponseSchema):
    """DescribeUDisk - 获取UDisk实例"""

    fields = {
        "DataSet": fields.List(
            models.UDiskDataSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUDiskPrice

获取UDisk实例价格信息
"""


class DescribeUDiskPriceRequestSchema(schema.RequestSchema):
    """DescribeUDiskPrice - 获取UDisk实例价格信息"""

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUDiskPriceResponseSchema(schema.ResponseSchema):
    """DescribeUDiskPrice - 获取UDisk实例价格信息"""

    fields = {
        "DataSet": fields.List(
            models.UDiskPriceDataSetSchema(),
            required=False,
            load_from="DataSet",
        )
    }


"""
API: DescribeUDiskSnapshot

获取UDisk快照
"""


class DescribeUDiskSnapshotRequestSchema(schema.RequestSchema):
    """DescribeUDiskSnapshot - 获取UDisk快照"""

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SnapshotId": fields.Str(required=False, dump_to="SnapshotId"),
        "UDiskId": fields.Str(required=False, dump_to="UDiskId"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DescribeUDiskSnapshotResponseSchema(schema.ResponseSchema):
    """DescribeUDiskSnapshot - 获取UDisk快照"""

    fields = {
        "DataSet": fields.List(
            models.UDiskSnapshotSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: DescribeUDiskUpgradePrice

获取UDisk升级价格信息
"""


class DescribeUDiskUpgradePriceRequestSchema(schema.RequestSchema):
    """DescribeUDiskUpgradePrice - 获取UDisk升级价格信息"""

    fields = {
        "DiskType": fields.Str(required=False, dump_to="DiskType"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "SourceId": fields.Str(required=True, dump_to="SourceId"),
        "UDataArkMode": fields.Str(required=False, dump_to="UDataArkMode"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DescribeUDiskUpgradePriceResponseSchema(schema.ResponseSchema):
    """DescribeUDiskUpgradePrice - 获取UDisk升级价格信息"""

    fields = {
        "OriginalPrice": fields.Int(required=False, load_from="OriginalPrice"),
        "Price": fields.Int(required=False, load_from="Price"),
    }


"""
API: DetachUDisk

卸载某个已经挂载在指定UHost实例上的UDisk
"""


class DetachUDiskRequestSchema(schema.RequestSchema):
    """DetachUDisk - 卸载某个已经挂载在指定UHost实例上的UDisk"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "UHostId": fields.Str(required=True, dump_to="UHostId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class DetachUDiskResponseSchema(schema.ResponseSchema):
    """DetachUDisk - 卸载某个已经挂载在指定UHost实例上的UDisk"""

    fields = {
        "UDiskId": fields.Str(required=False, load_from="UDiskId"),
        "UHostId": fields.Str(required=False, load_from="UHostId"),
    }


"""
API: RenameUDisk

重命名UDisk
"""


class RenameUDiskRequestSchema(schema.RequestSchema):
    """RenameUDisk - 重命名UDisk"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "UDiskName": fields.Str(required=True, dump_to="UDiskName"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class RenameUDiskResponseSchema(schema.ResponseSchema):
    """RenameUDisk - 重命名UDisk"""

    fields = {}


"""
API: ResizeUDisk

调整UDisk容量
"""


class ResizeUDiskRequestSchema(schema.RequestSchema):
    """ResizeUDisk - 调整UDisk容量"""

    fields = {
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Size": fields.Int(required=True, dump_to="Size"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class ResizeUDiskResponseSchema(schema.ResponseSchema):
    """ResizeUDisk - 调整UDisk容量"""

    fields = {}


"""
API: RestoreUDisk

从备份恢复数据至UDisk
"""


class RestoreUDiskRequestSchema(schema.RequestSchema):
    """RestoreUDisk - 从备份恢复数据至UDisk"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "SnapshotId": fields.Str(required=False, dump_to="SnapshotId"),
        "SnapshotTime": fields.Int(required=False, dump_to="SnapshotTime"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class RestoreUDiskResponseSchema(schema.ResponseSchema):
    """RestoreUDisk - 从备份恢复数据至UDisk"""

    fields = {}


"""
API: SetUDiskUDataArkMode

设置UDisk数据方舟的状态
"""


class SetUDiskUDataArkModeRequestSchema(schema.RequestSchema):
    """SetUDiskUDataArkMode - 设置UDisk数据方舟的状态"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "UDataArkMode": fields.Str(required=True, dump_to="UDataArkMode"),
        "UDiskId": fields.Str(required=True, dump_to="UDiskId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class SetUDiskUDataArkModeResponseSchema(schema.ResponseSchema):
    """SetUDiskUDataArkMode - 设置UDisk数据方舟的状态"""

    fields = {}
