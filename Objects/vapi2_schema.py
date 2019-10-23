import sgqlc.types
import sgqlc.types.datetime

vapi2_schema = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
class AggregationWindow(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('last3h', 'last24h', 'last7d', 'last14d')


class AnnotationType(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('user', 'system')


class ApplicationFilterAttribute(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('ssid', 'custom')


Boolean = sgqlc.types.Boolean


class BooleanOperator(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('OR', 'AND')


class CustomGroupType(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('ap_group', 'custom', 'floor', 'building')


Date = sgqlc.types.datetime.DateTime


class FilterableAttribute(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('ap', 'apGroup', 'apModel', 'customGroup', 'model', 'os', 'rfBand', 'ssid', 'isWireless', 'routerInterface', 'radiusServer', 'dhcpServer', 'vlan', 'dnsServer')


Float = sgqlc.types.Float

Int = sgqlc.types.Int


class IoTBenchmark(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('DataRateComparison', 'RxDataRateComparison', 'TxDataRateComparison', 'TimeInUseComparison', 'HostsComparison', 'InternalHostsComparison', 'ExternalHostsComparison', 'VisitedHostsThreatComparison', 'VisitedHostsGeographicComparison', 'DeviceProtocolsUsedComparison')


class IoTStatsAggField(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('host', 'essid', 'vlan')


class Long(sgqlc.types.Scalar):
    __schema__ = vapi2_schema


class Metric(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('wifiPerformanceQoE', 'webPerformanceQoE')


class MetricCategory(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('wifi', 'dns', 'dhcp', 'radius', 'arp', 'web', 'apps', 'security', 'abnormality', 'other')


class SortingOrder(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('ASC', 'DESC')


String = sgqlc.types.String


class UsageLevel(sgqlc.types.Enum):
    __schema__ = vapi2_schema
    __choices__ = ('low', 'medium', 'high')


########################################################################
# Input Objects
########################################################################
class AppFilter(sgqlc.types.Input):
    __schema__ = vapi2_schema
    filter_attribute = sgqlc.types.Field(sgqlc.types.non_null(ApplicationFilterAttribute), graphql_name='filterAttribute')
    filter_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filterValue')


class FieldFilter(sgqlc.types.Input):
    __schema__ = vapi2_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='field')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class FieldFilters(sgqlc.types.Input):
    __schema__ = vapi2_schema
    op = sgqlc.types.Field(BooleanOperator, graphql_name='op')
    filters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilter))), graphql_name='filters')


class Filter(sgqlc.types.Input):
    __schema__ = vapi2_schema
    filter_attribute = sgqlc.types.Field(sgqlc.types.non_null(FilterableAttribute), graphql_name='filterAttribute')
    filter_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filterValue')


########################################################################
# Output Objects and Interfaces
########################################################################
class AccessPointNeighbor(sgqlc.types.Type):
    __schema__ = vapi2_schema
    ap_mac_addr = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='apMacAddr')
    num_devices = sgqlc.types.Field(Int, graphql_name='numDevices')
    snr_db = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='snrDb')
    channel = sgqlc.types.Field(Int, graphql_name='channel')


class AccessPointNoiseSource(sgqlc.types.Type):
    __schema__ = vapi2_schema
    noise_source = sgqlc.types.Field(String, graphql_name='noiseSource')
    rssi_dbm = sgqlc.types.Field(Int, graphql_name='rssiDbm')


class AccessPointRadio(sgqlc.types.Type):
    __schema__ = vapi2_schema
    radio_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='radioNumber')
    radio_channel = sgqlc.types.Field(Int, graphql_name='radioChannel')
    rf_band = sgqlc.types.Field(Int, graphql_name='rfBand')
    rf_channel_width = sgqlc.types.Field(String, graphql_name='rfChannelWidth')
    rf_protocol = sgqlc.types.Field(String, graphql_name='rfProtocol')
    radio_noise_floor = sgqlc.types.Field(Int, graphql_name='radioNoiseFloor')
    tx_power_in_dbm = sgqlc.types.Field(Int, graphql_name='txPowerInDbm')
    tx_power_level = sgqlc.types.Field(Int, graphql_name='txPowerLevel')
    radio_mode = sgqlc.types.Field(String, graphql_name='radioMode')
    radio_ht_mode = sgqlc.types.Field(String, graphql_name='radioHtMode')
    radio_phy_type = sgqlc.types.Field(String, graphql_name='radioPhyType')
    admin_status = sgqlc.types.Field(Boolean, graphql_name='adminStatus')
    num_devices = sgqlc.types.Field(Int, graphql_name='numDevices')
    bad_roams = sgqlc.types.Field(Int, graphql_name='badRoams')
    median_dwell_time_ms = sgqlc.types.Field(Long, graphql_name='medianDwellTimeMs')
    bssids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='bssids')
    essids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='essids')
    ap_radio_status = sgqlc.types.Field(String, graphql_name='apRadioStatus')
    neighbor_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AccessPointNeighbor)), graphql_name='neighborList')
    rogue_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AccessPointRogue')), graphql_name='rogueList')
    noise_source_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AccessPointNoiseSource)), graphql_name='noiseSourceList')
    associated_client_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RadioAssociatedClient')), graphql_name='associatedClientList')


class AccessPointRogue(sgqlc.types.Type):
    __schema__ = vapi2_schema
    bssid_mac_addr = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bssidMacAddr')
    essid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='essid')
    snr_db = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='snrDb')


class ApplicationTopTalker(sgqlc.types.Type):
    __schema__ = vapi2_schema
    device = sgqlc.types.Field(sgqlc.types.non_null('Device'), graphql_name='device')
    agg_window = sgqlc.types.Field(String, graphql_name='aggWindow')
    agg_updated = sgqlc.types.Field(Date, graphql_name='aggUpdated')
    total_bytes = sgqlc.types.Field(Float, graphql_name='totalBytes')
    rx_bytes = sgqlc.types.Field(Float, graphql_name='rxBytes')
    tx_bytes = sgqlc.types.Field(Float, graphql_name='txBytes')


class AttributeChange(sgqlc.types.Type):
    __schema__ = vapi2_schema
    sample_time = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='sampleTime')
    attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='attribute')
    new_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newValue')
    old_value = sgqlc.types.Field(String, graphql_name='oldValue')
    related_entity = sgqlc.types.Field('NyansaEntity', graphql_name='relatedEntity')


class BaselineStats(sgqlc.types.Type):
    __schema__ = vapi2_schema
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    deviation_info = sgqlc.types.Field(sgqlc.types.non_null('DeviationInfo'), graphql_name='deviationInfo')


class ControllerInfo(sgqlc.types.Type):
    __schema__ = vapi2_schema
    model = sgqlc.types.Field(String, graphql_name='model')
    version = sgqlc.types.Field(String, graphql_name='version')
    build = sgqlc.types.Field(String, graphql_name='build')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    serial_num = sgqlc.types.Field(String, graphql_name='serialNum')
    description = sgqlc.types.Field(String, graphql_name='description')


class DeviationInfo(sgqlc.types.Type):
    __schema__ = vapi2_schema
    p_mean = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pMean')
    p_sigma = sgqlc.types.Field(Float, graphql_name='pSigma')


class DeviceTypeDetails(sgqlc.types.Type):
    __schema__ = vapi2_schema
    os = sgqlc.types.Field(String, graphql_name='os')
    os_version = sgqlc.types.Field(String, graphql_name='osVersion')
    os_and_version = sgqlc.types.Field(String, graphql_name='osAndVersion')
    device_class = sgqlc.types.Field(String, graphql_name='deviceClass')
    model = sgqlc.types.Field(String, graphql_name='model')
    browser = sgqlc.types.Field(String, graphql_name='browser')
    user_agent = sgqlc.types.Field(String, graphql_name='userAgent')


class EntityAggregatedMetrics(sgqlc.types.Type):
    __schema__ = vapi2_schema
    total_bytes = sgqlc.types.Field(Float, graphql_name='total_bytes')
    tx_bytes = sgqlc.types.Field(Float, graphql_name='tx_bytes')
    rx_bytes = sgqlc.types.Field(Float, graphql_name='rx_bytes')
    total_pkts = sgqlc.types.Field(Float, graphql_name='total_pkts')
    tx_pkts = sgqlc.types.Field(Float, graphql_name='tx_pkts')
    rx_pkts = sgqlc.types.Field(Float, graphql_name='rx_pkts')


class HasAccessPoint(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    ap_descriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='apDescriptions')


class HasCustomGroup(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    custom_group_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='customGroupNames')


class HasLocation(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class HasNsUser(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    ns_user_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='nsUserNames')


class HasVoyanceUrl(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    voyance_url = sgqlc.types.Field(String, graphql_name='voyanceUrl')


class HistogramBucket(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class IncidentRemediations(sgqlc.types.Type):
    __schema__ = vapi2_schema
    root_cause = sgqlc.types.Field(String, graphql_name='rootCause')
    next_steps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='nextSteps')
    uuids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='uuids')


class IncidentTopAttribute(sgqlc.types.Type):
    __schema__ = vapi2_schema
    attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='attribute')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    affected_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='affectedCount')
    percent_affected = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='percentAffected')


class IoTBenchmarkComparison(sgqlc.types.Type):
    __schema__ = vapi2_schema
    model = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='model')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    benchmark = sgqlc.types.Field(String, graphql_name='benchmark')
    you = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(HistogramBucket))), graphql_name='you')
    others = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(HistogramBucket))), graphql_name='others')


class IoTSingleAggStats(sgqlc.types.Type):
    __schema__ = vapi2_schema
    host = sgqlc.types.Field(String, graphql_name='host')
    host_internal = sgqlc.types.Field(Boolean, graphql_name='hostInternal')
    essid = sgqlc.types.Field(String, graphql_name='essid')
    vlan = sgqlc.types.Field(String, graphql_name='vlan')
    total_bytes = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalBytes')
    rx_bytes = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='rxBytes')
    tx_bytes = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='txBytes')
    device_initiated_connections = sgqlc.types.Field(Float, graphql_name='deviceInitiatedConnections')
    total_connections = sgqlc.types.Field(Float, graphql_name='totalConnections')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')


class Location(sgqlc.types.Type):
    __schema__ = vapi2_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    controller_ips = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='controllerIps')
    subnets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subnets')
    aps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='aps')
    ap_regex_value = sgqlc.types.Field(String, graphql_name='apRegexValue')
    router_interface_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='routerInterfaceIds')


class NyansaEntity(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    description = sgqlc.types.Field(String, graphql_name='description')
    last_updated = sgqlc.types.Field(Date, graphql_name='lastUpdated')
    created_at = sgqlc.types.Field(Date, graphql_name='createdAt')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    mac_addr = sgqlc.types.Field(String, graphql_name='macAddr')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class NyansaGraphQLQuery(sgqlc.types.Type):
    __schema__ = vapi2_schema
    access_point_list = sgqlc.types.Field(sgqlc.types.non_null('AccessPointList'), graphql_name='accessPointList', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                          )
    device_list = sgqlc.types.Field(sgqlc.types.non_null('DeviceList'), graphql_name='deviceList', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                    )
    server_list = sgqlc.types.Field(sgqlc.types.non_null('ServerList'), graphql_name='serverList', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                    )
    controller_list = sgqlc.types.Field(sgqlc.types.non_null('ControllerList'), graphql_name='controllerList', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                        )
    application_list = sgqlc.types.Field(sgqlc.types.non_null('ApplicationList'), graphql_name='applicationList', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['totalBytes'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('agg_window', sgqlc.types.Arg(AggregationWindow, graphql_name='aggWindow', default='last24h')),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('app_filter', sgqlc.types.Arg(AppFilter, graphql_name='appFilter', default=None)),
    ))
                                         )
    omnisearch_list = sgqlc.types.Field(sgqlc.types.non_null('NyansaEntityList'), graphql_name='omnisearchList', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='search', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
    ))
                                        )
    location_list = sgqlc.types.Field(sgqlc.types.non_null('LocationList'), graphql_name='locationList', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='names', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=None)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='ASC')),
    ))
                                      )
    custom_group_list = sgqlc.types.Field(sgqlc.types.non_null('CustomGroupList'), graphql_name='customGroupList', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='names', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=None)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='ASC')),
        ('type_filter', sgqlc.types.Arg(CustomGroupType, graphql_name='typeFilter', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
    ))
                                          )
    incident_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Incident'))), graphql_name='incidentList', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('metric_category', sgqlc.types.Arg(MetricCategory, graphql_name='metricCategory', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
    ))
                                      )
    device_problems_list = sgqlc.types.Field(sgqlc.types.non_null('DeviceProblemsList'), graphql_name='deviceProblemsList', args=sgqlc.types.ArgDict((
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids', default=None)),
        ('metric_category', sgqlc.types.Arg(MetricCategory, graphql_name='metricCategory', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['incidentRatio'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
    ))
                                             )
    affected_client_hours_distribution = sgqlc.types.Field(sgqlc.types.non_null('AffectedClientHoursList'), graphql_name='affectedClientHoursDistribution', args=sgqlc.types.ArgDict((
        ('metric_category', sgqlc.types.Arg(MetricCategory, graphql_name='metricCategory', default=None)),
        ('metric_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metricIds', default=None)),
        ('agg_fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='aggFields', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                                           )
    global_advisory_list = sgqlc.types.Field(sgqlc.types.non_null('GlobalAdvisoryList'), graphql_name='globalAdvisoryList', args=sgqlc.types.ArgDict((
        ('sort_by', sgqlc.types.Arg(String, graphql_name='sortBy', default=None)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='ASC')),
        ('metric_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metricIds', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
    ))
                                             )
    remediation_list = sgqlc.types.Field(sgqlc.types.non_null('RemediationList'), graphql_name='remediationList', args=sgqlc.types.ArgDict((
        ('metric_category', sgqlc.types.Arg(MetricCategory, graphql_name='metricCategory', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['clientHours'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                         )
    baseline_stats_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BaselineStats))), graphql_name='baselineStatsList', args=sgqlc.types.ArgDict((
        ('metric_name', sgqlc.types.Arg(Metric, graphql_name='metricName', default=None)),
        ('metric_id', sgqlc.types.Arg(String, graphql_name='metricId', default=None)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='ASC')),
        ('usage_level', sgqlc.types.Arg(UsageLevel, graphql_name='usageLevel', default='high')),
        ('location_filter', sgqlc.types.Arg(String, graphql_name='locationFilter', default=None)),
        ('filter', sgqlc.types.Arg(Filter, graphql_name='filter', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
    ))
                                            )
    usage_history_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageTsSample'))), graphql_name='usageHistoryList', args=sgqlc.types.ArgDict((
        ('metric_name', sgqlc.types.Arg(Metric, graphql_name='metricName', default=None)),
        ('metric_id', sgqlc.types.Arg(String, graphql_name='metricId', default=None)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='ASC')),
        ('location_filter', sgqlc.types.Arg(String, graphql_name='locationFilter', default=None)),
        ('filter', sgqlc.types.Arg(Filter, graphql_name='filter', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
    ))
                                           )
    annotation_list = sgqlc.types.Field(sgqlc.types.non_null('AnnotationList'), graphql_name='annotationList', args=sgqlc.types.ArgDict((
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='ASC')),
        ('annotation_group', sgqlc.types.Arg(AnnotationType, graphql_name='annotationGroup', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('metric_category', sgqlc.types.Arg(MetricCategory, graphql_name='metricCategory', default=None)),
        ('custom_group_filter', sgqlc.types.Arg(String, graphql_name='customGroupFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
        ('metric_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metricIds', default=None)),
        ('usage_level', sgqlc.types.Arg(UsageLevel, graphql_name='usageLevel', default='high')),
    ))
                                        )
    iot_outlier_list = sgqlc.types.Field(sgqlc.types.non_null('IoTOutlierList'), graphql_name='iotOutlierList', args=sgqlc.types.ArgDict((
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['time'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('agg_window', sgqlc.types.Arg(AggregationWindow, graphql_name='aggWindow', default='last24h')),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                         )
    iot_device_stats_list = sgqlc.types.Field(sgqlc.types.non_null('IoTDeviceStatsList'), graphql_name='iotDeviceStatsList', args=sgqlc.types.ArgDict((
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['totalBytes'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('agg_window', sgqlc.types.Arg(AggregationWindow, graphql_name='aggWindow', default='last24h')),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                              )
    iot_group_stats_list = sgqlc.types.Field(sgqlc.types.non_null('IoTGroupStatsList'), graphql_name='iotGroupStatsList', args=sgqlc.types.ArgDict((
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['totalBytes'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('agg_window', sgqlc.types.Arg(AggregationWindow, graphql_name='aggWindow', default='last24h')),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                             )
    iot_single_device_stats = sgqlc.types.Field(sgqlc.types.non_null('IoTSingleStats'), graphql_name='iotSingleDeviceStats', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uuid', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('agg_field', sgqlc.types.Arg(IoTStatsAggField, graphql_name='aggField', default='host')),
        ('slice_by_protocol', sgqlc.types.Arg(Boolean, graphql_name='sliceByProtocol', default=True)),
        ('sort_by', sgqlc.types.Arg(String, graphql_name='sortBy', default='totalBytes')),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('location_filter', sgqlc.types.Arg(String, graphql_name='locationFilter', default=None)),
    ))
                                                )
    iot_single_group_stats = sgqlc.types.Field(sgqlc.types.non_null('IoTSingleStats'), graphql_name='iotSingleGroupStats', args=sgqlc.types.ArgDict((
        ('model', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='model', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('agg_field', sgqlc.types.Arg(IoTStatsAggField, graphql_name='aggField', default='host')),
        ('slice_by_protocol', sgqlc.types.Arg(Boolean, graphql_name='sliceByProtocol', default=True)),
        ('sort_by', sgqlc.types.Arg(String, graphql_name='sortBy', default='totalBytes')),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('location_filter', sgqlc.types.Arg(String, graphql_name='locationFilter', default=None)),
    ))
                                               )
    iot_benchmark_comparisons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IoTBenchmarkComparison))), graphql_name='iotBenchmarkComparisons', args=sgqlc.types.ArgDict((
        ('model', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='model', default=None)),
        ('benchmark', sgqlc.types.Arg(IoTBenchmark, graphql_name='benchmark', default=None)),
    ))
                                                  )
    top_url_list = sgqlc.types.Field(sgqlc.types.non_null('TopUrlsList'), graphql_name='topUrlList', args=sgqlc.types.ArgDict((
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('is_internal', sgqlc.types.Arg(Boolean, graphql_name='isInternal', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
        ('filters', sgqlc.types.Arg(FieldFilters, graphql_name='filters', default=None)),
    ))
                                     )


class PaginatedResults(sgqlc.types.Interface):
    __schema__ = vapi2_schema
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PerformanceChange(sgqlc.types.Type):
    __schema__ = vapi2_schema
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    change = sgqlc.types.Field(Float, graphql_name='change')


class RadioAssociatedClient(sgqlc.types.Type):
    __schema__ = vapi2_schema
    mac_addr = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='macAddr')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    ten_min_byte_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='tenMinByteCount')


class RelatedAccessPoints(sgqlc.types.Type):
    __schema__ = vapi2_schema
    ap_mac_addr = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='apMacAddr')
    last_seen = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='lastSeen')


class RelatedAttributes(sgqlc.types.Type):
    __schema__ = vapi2_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='timestamp')


class RemediationBucket(sgqlc.types.Type):
    __schema__ = vapi2_schema
    bucket = sgqlc.types.Field(String, graphql_name='bucket')
    client_hours = sgqlc.types.Field(Float, graphql_name='clientHours')


class RemediationClientHoursByUuid(sgqlc.types.Type):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    client_hours = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='clientHours')


class RemediationDistributions(sgqlc.types.Type):
    __schema__ = vapi2_schema
    bucket_type = sgqlc.types.Field(String, graphql_name='bucketType')
    distrib = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RemediationBucket)), graphql_name='distrib')


class SystemAnnotationProperties(sgqlc.types.Type):
    __schema__ = vapi2_schema
    time = sgqlc.types.Field(Date, graphql_name='time')
    profile_id = sgqlc.types.Field(String, graphql_name='profileId')
    profile_value = sgqlc.types.Field(String, graphql_name='profileValue')
    ap_group = sgqlc.types.Field(String, graphql_name='apGroup')
    controller_ip = sgqlc.types.Field(String, graphql_name='controllerIp')
    metric_id = sgqlc.types.Field(String, graphql_name='metricId')
    locations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locations')
    old_value = sgqlc.types.Field(String, graphql_name='oldValue')
    value = sgqlc.types.Field(String, graphql_name='value')


class TopUrls(sgqlc.types.Type):
    __schema__ = vapi2_schema
    is_internal = sgqlc.types.Field(Boolean, graphql_name='isInternal')
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='host')
    num_bytes = sgqlc.types.Field(Long, graphql_name='numBytes')
    num_bytes_sent = sgqlc.types.Field(Long, graphql_name='numBytesSent')
    num_bytes_rcvd = sgqlc.types.Field(Long, graphql_name='numBytesRcvd')


class UsageTsSample(sgqlc.types.Type):
    __schema__ = vapi2_schema
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    value = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='value')


class AccessPoint(sgqlc.types.Type, NyansaEntity, HasLocation, HasVoyanceUrl):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    mac_addr = sgqlc.types.Field(String, graphql_name='macAddr')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    ap_name = sgqlc.types.Field(String, graphql_name='apName')
    ap_model = sgqlc.types.Field(String, graphql_name='apModel')
    ap_group = sgqlc.types.Field(String, graphql_name='apGroup')
    last_updated = sgqlc.types.Field(Date, graphql_name='lastUpdated')
    custom_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='customGroups')
    ap_location = sgqlc.types.Field(String, graphql_name='apLocation')
    ap_status = sgqlc.types.Field(Boolean, graphql_name='apStatus')
    num_devices = sgqlc.types.Field(Int, graphql_name='numDevices')
    description = sgqlc.types.Field(String, graphql_name='description')
    controller_ip = sgqlc.types.Field(String, graphql_name='controllerIp')
    last_ap_reboot_reason = sgqlc.types.Field(String, graphql_name='lastApRebootReason')
    created_at = sgqlc.types.Field(Date, graphql_name='createdAt')
    ap_radios = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessPointRadio))), graphql_name='apRadios')
    affected_client_hours_distribution = sgqlc.types.Field(sgqlc.types.non_null('AffectedClientHoursList'), graphql_name='affectedClientHoursDistribution', args=sgqlc.types.ArgDict((
        ('metric_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metricIds', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
    ))
                                                           )
    attribute_changes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttributeChange))), graphql_name='attributeChanges', args=sgqlc.types.ArgDict((
        ('attribute_names', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='attributeNames', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
    ))
                                          )
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')
    voyance_url = sgqlc.types.Field(String, graphql_name='voyanceUrl')


class AccessPointList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    access_points = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessPoint))), graphql_name='accessPoints')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AffectedClientHours(sgqlc.types.Type, HasLocation, HasCustomGroup, HasAccessPoint):
    __schema__ = vapi2_schema
    client_hours = sgqlc.types.Field(Int, graphql_name='clientHours')
    usage_hours = sgqlc.types.Field(Int, graphql_name='usageHours')
    metric_id = sgqlc.types.Field(String, graphql_name='metricId')
    root_cause = sgqlc.types.Field(String, graphql_name='rootCause')
    rf_band = sgqlc.types.Field(Int, graphql_name='rfBand')
    ap_mac_addr = sgqlc.types.Field(String, graphql_name='apMacAddr')
    ap_mac_addr_radio = sgqlc.types.Field(String, graphql_name='apMacAddrRadio')
    ap_model = sgqlc.types.Field(String, graphql_name='apModel')
    essid = sgqlc.types.Field(String, graphql_name='essid')
    os = sgqlc.types.Field(String, graphql_name='os')
    ap_group = sgqlc.types.Field(String, graphql_name='apGroup')
    radio_channel = sgqlc.types.Field(Int, graphql_name='radioChannel')
    ch_change_old_val = sgqlc.types.Field(Int, graphql_name='chChange_oldVal')
    all_dhcp_server_uuids = sgqlc.types.Field(String, graphql_name='allDhcpServerUuids')
    all_dns_server_uuids = sgqlc.types.Field(String, graphql_name='allDnsServerUuids')
    all_radius_server_uuids = sgqlc.types.Field(String, graphql_name='allRadiusServerUuids')
    all_router_interface_ids = sgqlc.types.Field(String, graphql_name='allRouterInterfaceIds')
    connectivity_arp_vlan_id = sgqlc.types.Field(String, graphql_name='connectivity_arpVlanId')
    connectivity_dhcp_server_ip = sgqlc.types.Field(String, graphql_name='connectivity_dhcpServerIp')
    connectivity_dns_server_ip = sgqlc.types.Field(String, graphql_name='connectivity_dnsServerIp')
    connectivity_radius_essid = sgqlc.types.Field(String, graphql_name='connectivity_radiusEssid')
    connectivity_radius_server_ip = sgqlc.types.Field(String, graphql_name='connectivity_radiusServerIp')
    dhcp_vlan_id = sgqlc.types.Field(String, graphql_name='dhcpVlanId')
    is_wireless = sgqlc.types.Field(Boolean, graphql_name='isWireless')
    custom_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='customGroups')
    metric_description = sgqlc.types.Field(String, graphql_name='metricDescription')
    affected_ratio = sgqlc.types.Field(Float, graphql_name='affectedRatio')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')
    custom_group_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='customGroupNames')
    ap_descriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='apDescriptions')


class AffectedClientHoursList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    affected_client_hours = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AffectedClientHours))), graphql_name='affectedClientHours')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Annotation(sgqlc.types.Type, HasLocation, HasCustomGroup, HasNsUser):
    __schema__ = vapi2_schema
    type = sgqlc.types.Field(sgqlc.types.non_null(AnnotationType), graphql_name='type')
    metric_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MetricCategory)), graphql_name='metricCategories')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    time = sgqlc.types.Field(Date, graphql_name='time')
    body = sgqlc.types.Field(String, graphql_name='body')
    details = sgqlc.types.Field(SystemAnnotationProperties, graphql_name='details')
    performance_change = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PerformanceChange)), graphql_name='performanceChange')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')
    custom_group_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='customGroupNames')
    ns_user_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='nsUserNames')


class AnnotationList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    annotations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Annotation))), graphql_name='annotations')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Application(sgqlc.types.Type, NyansaEntity, HasLocation):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    app_name = sgqlc.types.Field(String, graphql_name='appName')
    last_updated = sgqlc.types.Field(Date, graphql_name='lastUpdated')
    created_at = sgqlc.types.Field(Date, graphql_name='createdAt')
    user_count = sgqlc.types.Field(Int, graphql_name='userCount')
    agg_window = sgqlc.types.Field(String, graphql_name='aggWindow')
    agg_updated = sgqlc.types.Field(Date, graphql_name='aggUpdated')
    total_bytes = sgqlc.types.Field(Float, graphql_name='totalBytes')
    rx_bytes = sgqlc.types.Field(Float, graphql_name='rxBytes')
    tx_bytes = sgqlc.types.Field(Float, graphql_name='txBytes')
    top_talkers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApplicationTopTalker))), graphql_name='topTalkers', args=sgqlc.types.ArgDict((
        ('top', sgqlc.types.Arg(Int, graphql_name='top', default=10)),
    ))
                                    )
    description = sgqlc.types.Field(String, graphql_name='description')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    mac_addr = sgqlc.types.Field(String, graphql_name='macAddr')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class ApplicationList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    applications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Application))), graphql_name='applications')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CategoricalHistogramBucket(sgqlc.types.Type, HistogramBucket):
    __schema__ = vapi2_schema
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class Controller(sgqlc.types.Type, NyansaEntity, HasLocation):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    description = sgqlc.types.Field(String, graphql_name='description')
    last_updated = sgqlc.types.Field(Date, graphql_name='lastUpdated')
    created_at = sgqlc.types.Field(Date, graphql_name='createdAt')
    controller_ip = sgqlc.types.Field(String, graphql_name='controllerIp')
    controller_info = sgqlc.types.Field(ControllerInfo, graphql_name='controllerInfo')
    mgmt = sgqlc.types.Field(Boolean, graphql_name='mgmt')
    nas = sgqlc.types.Field(Boolean, graphql_name='nas')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    mac_addr = sgqlc.types.Field(String, graphql_name='macAddr')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class ControllerList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    controllers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Controller))), graphql_name='controllers')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CustomGroup(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    group_type = sgqlc.types.Field(CustomGroupType, graphql_name='groupType')
    expression = sgqlc.types.Field(String, graphql_name='expression')
    related_devices = sgqlc.types.Field(sgqlc.types.non_null('DeviceList'), graphql_name='relatedDevices', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
    ))
                                        )
    related_access_points = sgqlc.types.Field(sgqlc.types.non_null(AccessPointList), graphql_name='relatedAccessPoints', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
    ))
                                              )
    affected_client_hours = sgqlc.types.Field(AffectedClientHours, graphql_name='affectedClientHours', args=sgqlc.types.ArgDict((
        ('metric_category', sgqlc.types.Arg(MetricCategory, graphql_name='metricCategory', default=None)),
        ('metric_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metricIds', default=None)),
    ))
                                              )
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class CustomGroupList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    custom_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CustomGroup))), graphql_name='customGroups')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Device(sgqlc.types.Type, NyansaEntity, HasLocation, HasVoyanceUrl):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    mac_addr = sgqlc.types.Field(String, graphql_name='macAddr')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    hostname = sgqlc.types.Field(String, graphql_name='hostname')
    user_name = sgqlc.types.Field(String, graphql_name='userName')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    is_wireless = sgqlc.types.Field(Boolean, graphql_name='isWireless')
    ap_mac_addr = sgqlc.types.Field(String, graphql_name='apMacAddr')
    ap_name = sgqlc.types.Field(String, graphql_name='apName')
    ap_group = sgqlc.types.Field(String, graphql_name='apGroup')
    rf_band = sgqlc.types.Field(Int, graphql_name='rfBand')
    radio_channel = sgqlc.types.Field(Int, graphql_name='radioChannel')
    ch_width = sgqlc.types.Field(String, graphql_name='chWidth')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    essid = sgqlc.types.Field(String, graphql_name='essid')
    bssid = sgqlc.types.Field(String, graphql_name='bssid')
    network = sgqlc.types.Field(String, graphql_name='network')
    noise_on_ap = sgqlc.types.Field(Int, graphql_name='noiseOnAp')
    is_band_str_on_ap = sgqlc.types.Field(Boolean, graphql_name='isBandStrOnAp')
    is_dfs_on_ap = sgqlc.types.Field(Boolean, graphql_name='isDfsOnAp')
    ap_model = sgqlc.types.Field(String, graphql_name='apModel')
    snr_db = sgqlc.types.Field(Int, graphql_name='snrDb')
    radio_tech_type = sgqlc.types.Field(String, graphql_name='radioTechType')
    is5ghz_capable = sgqlc.types.Field(Boolean, graphql_name='is5ghzCapable')
    is_dfs_capable = sgqlc.types.Field(Boolean, graphql_name='isDfsCapable')
    is_on_dual_band_ap = sgqlc.types.Field(Boolean, graphql_name='isOnDualBandAp')
    is_lb_on_ap = sgqlc.types.Field(Boolean, graphql_name='isLbOnAp')
    ap_dwell_time_ms = sgqlc.types.Field(Long, graphql_name='apDwellTimeMs')
    controller_ip = sgqlc.types.Field(String, graphql_name='controllerIp')
    device_type_details = sgqlc.types.Field(DeviceTypeDetails, graphql_name='deviceTypeDetails')
    is_iot_device = sgqlc.types.Field(Boolean, graphql_name='isIotDevice')
    is_critical = sgqlc.types.Field(Boolean, graphql_name='isCritical')
    last_updated = sgqlc.types.Field(Date, graphql_name='lastUpdated')
    created_at = sgqlc.types.Field(Date, graphql_name='createdAt')
    wanna_cry_last_time = sgqlc.types.Field(Date, graphql_name='wannaCryLastTime')
    access_point_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RelatedAccessPoints))), graphql_name='accessPointHistory')
    radio_tech_type_description = sgqlc.types.Field(String, graphql_name='radioTechTypeDescription')
    radio_tech_type_channel_width = sgqlc.types.Field(String, graphql_name='radioTechTypeChannelWidth')
    related_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RelatedAttributes))), graphql_name='relatedAttributes', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
    ))
                                           )
    attribute_changes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttributeChange))), graphql_name='attributeChanges', args=sgqlc.types.ArgDict((
        ('attribute_names', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='attributeNames', default=None)),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(Date, graphql_name='toDate', default=None)),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
    ))
                                          )
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')
    voyance_url = sgqlc.types.Field(String, graphql_name='voyanceUrl')


class DeviceList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    devices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Device))), graphql_name='devices')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeviceProblems(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    usage_hours = sgqlc.types.Field(Int, graphql_name='usageHours')
    incident_hours = sgqlc.types.Field(Int, graphql_name='incidentHours')
    incident_ratio = sgqlc.types.Field(Float, graphql_name='incidentRatio')
    sample_time = sgqlc.types.Field(Date, graphql_name='sampleTime')
    metric_description = sgqlc.types.Field(String, graphql_name='metricDescription')
    metric_id = sgqlc.types.Field(String, graphql_name='metricId')
    device = sgqlc.types.Field(Device, graphql_name='device')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class DeviceProblemsList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    device_problems = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeviceProblems))), graphql_name='deviceProblems')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GlobalAdvisory(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    metric_signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metricSignature')
    num_affected = sgqlc.types.Field(Int, graphql_name='numAffected')
    num_entities = sgqlc.types.Field(Int, graphql_name='numEntities')
    start_time = sgqlc.types.Field(Date, graphql_name='startTime')
    percent_affected = sgqlc.types.Field(Float, graphql_name='percentAffected')
    description = sgqlc.types.Field(String, graphql_name='description')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')
    affected_entities = sgqlc.types.Field(sgqlc.types.non_null('NyansaEntityList'), graphql_name='affectedEntities', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
    ))
                                          )
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class GlobalAdvisoryList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    global_advisories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GlobalAdvisory))), graphql_name='globalAdvisories')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Incident(sgqlc.types.Type, HasLocation, HasVoyanceUrl):
    __schema__ = vapi2_schema
    description = sgqlc.types.Field(String, graphql_name='description')
    metric_description = sgqlc.types.Field(String, graphql_name='metricDescription')
    incident_start_time = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='incidentStartTime')
    incident_end_time = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='incidentEndTime')
    rank = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rank')
    unique_affected_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='uniqueAffectedCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    top_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IncidentTopAttribute))), graphql_name='topAttributes')
    details = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IncidentRemediations))), graphql_name='details')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')
    voyance_url = sgqlc.types.Field(String, graphql_name='voyanceUrl')


class IoTDeviceStats(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    agg_updated = sgqlc.types.Field(Date, graphql_name='aggUpdated')
    model = sgqlc.types.Field(String, graphql_name='model')
    device_class = sgqlc.types.Field(String, graphql_name='deviceClass')
    total_bytes = sgqlc.types.Field(Float, graphql_name='totalBytes')
    rx_bytes = sgqlc.types.Field(Float, graphql_name='rxBytes')
    tx_bytes = sgqlc.types.Field(Float, graphql_name='txBytes')
    avg_bytes_per_sec = sgqlc.types.Field(Float, graphql_name='avgBytesPerSec')
    avg_rx_bytes_per_sec = sgqlc.types.Field(Float, graphql_name='avgRxBytesPerSec')
    avg_tx_bytes_per_sec = sgqlc.types.Field(Float, graphql_name='avgTxBytesPerSec')
    total_time_secs = sgqlc.types.Field(Float, graphql_name='totalTimeSecs')
    num_hosts = sgqlc.types.Field(Int, graphql_name='numHosts')
    num_internal_hosts = sgqlc.types.Field(Int, graphql_name='numInternalHosts')
    num_external_hosts = sgqlc.types.Field(Int, graphql_name='numExternalHosts')
    essids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='essids')
    vlans = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='vlans')
    suspicious_hosts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='suspiciousHosts')
    high_risk_hosts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='highRiskHosts')
    hosts_geo = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hostsGeo')
    device = sgqlc.types.Field(Device, graphql_name='device')
    is_critical = sgqlc.types.Field(Boolean, graphql_name='isCritical')
    agg_window = sgqlc.types.Field(String, graphql_name='aggWindow')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class IoTDeviceStatsList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    iot_device_stats = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IoTDeviceStats))), graphql_name='iotDeviceStats')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IoTGroupStats(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    model = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='model')
    agg_updated = sgqlc.types.Field(Date, graphql_name='aggUpdated')
    device_class = sgqlc.types.Field(String, graphql_name='deviceClass')
    num_devices = sgqlc.types.Field(Int, graphql_name='numDevices')
    total_bytes = sgqlc.types.Field(Float, graphql_name='totalBytes')
    rx_bytes = sgqlc.types.Field(Float, graphql_name='rxBytes')
    tx_bytes = sgqlc.types.Field(Float, graphql_name='txBytes')
    avg_bytes_per_sec = sgqlc.types.Field(Float, graphql_name='avgBytesPerSec')
    avg_rx_bytes_per_sec = sgqlc.types.Field(Float, graphql_name='avgRxBytesPerSec')
    avg_tx_bytes_per_sec = sgqlc.types.Field(Float, graphql_name='avgTxBytesPerSec')
    total_time_secs = sgqlc.types.Field(Float, graphql_name='totalTimeSecs')
    num_hosts = sgqlc.types.Field(Int, graphql_name='numHosts')
    num_internal_hosts = sgqlc.types.Field(Int, graphql_name='numInternalHosts')
    num_external_hosts = sgqlc.types.Field(Int, graphql_name='numExternalHosts')
    num_internal_devices = sgqlc.types.Field(Int, graphql_name='numInternalDevices')
    num_external_devices = sgqlc.types.Field(Int, graphql_name='numExternalDevices')
    essids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='essids')
    vlans = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='vlans')
    protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='protocols')
    is_critical = sgqlc.types.Field(Boolean, graphql_name='isCritical')
    agg_window = sgqlc.types.Field(String, graphql_name='aggWindow')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class IoTGroupStatsList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    iot_group_stats = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IoTGroupStats))), graphql_name='iotGroupStats')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IoTOutlier(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    model = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='model')
    time = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='time')
    outlier_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outlierType')
    outlier_category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outlierCategory')
    outlier_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outlierReason')
    outlier_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outlierValue')
    bc_score = sgqlc.types.Field(Float, graphql_name='bcScore')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class IoTOutlierList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    io_toutliers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IoTOutlier))), graphql_name='ioTOutliers')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IoTSingleStats(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    device_class = sgqlc.types.Field(String, graphql_name='deviceClass')
    model = sgqlc.types.Field(String, graphql_name='model')
    stats = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IoTSingleAggStats))), graphql_name='stats')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class LocationList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    locations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Location))), graphql_name='locations')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class NumericHistogramBucket(sgqlc.types.Type, HistogramBucket):
    __schema__ = vapi2_schema
    lower_bound = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='lowerBound')
    upper_bound = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='upperBound')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class NyansaEntityList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    entities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NyansaEntity))), graphql_name='entities')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Remediation(sgqlc.types.Type, HasLocation):
    __schema__ = vapi2_schema
    metric_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metricId')
    sample_time = sgqlc.types.Field(Date, graphql_name='sampleTime')
    recommendation_type = sgqlc.types.Field(String, graphql_name='recommendationType')
    uuids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uuids')
    client_hours = sgqlc.types.Field(Long, graphql_name='clientHours')
    rf_band = sgqlc.types.Field(Int, graphql_name='rfBand')
    root_cause = sgqlc.types.Field(String, graphql_name='rootCause')
    distributions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RemediationDistributions)), graphql_name='distributions')
    metric_description = sgqlc.types.Field(String, graphql_name='metricDescription')
    remediation_client_hours_by_uuid = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RemediationClientHoursByUuid))), graphql_name='remediationClientHoursByUuid')
    remediation_uuid_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='remediationUuidType')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')


class RemediationList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    remediations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Remediation))), graphql_name='remediations')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Server(sgqlc.types.Type, NyansaEntity, HasLocation, HasVoyanceUrl):
    __schema__ = vapi2_schema
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    hostname = sgqlc.types.Field(String, graphql_name='hostname')
    description = sgqlc.types.Field(String, graphql_name='description')
    server_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='serverTypes')
    last_updated = sgqlc.types.Field(Date, graphql_name='lastUpdated')
    created_at = sgqlc.types.Field(Date, graphql_name='createdAt')
    related_devices = sgqlc.types.Field(sgqlc.types.non_null(DeviceList), graphql_name='relatedDevices', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sortBy', default=['lastUpdated'])),
        ('sort_order', sgqlc.types.Arg(SortingOrder, graphql_name='sortOrder', default='DESC')),
        ('from_date', sgqlc.types.Arg(Date, graphql_name='fromDate', default=None)),
        ('location_filter', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='locationFilter', default=None)),
    ))
                                        )
    ten_min_aggregated_metrics = sgqlc.types.Field(EntityAggregatedMetrics, graphql_name='tenMinAggregatedMetrics')
    one_hour_aggregated_metrics = sgqlc.types.Field(EntityAggregatedMetrics, graphql_name='oneHourAggregatedMetrics')
    one_day_aggregated_metrics = sgqlc.types.Field(EntityAggregatedMetrics, graphql_name='oneDayAggregatedMetrics')
    mac_addr = sgqlc.types.Field(String, graphql_name='macAddr')
    location_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locationNames')
    voyance_url = sgqlc.types.Field(String, graphql_name='voyanceUrl')


class ServerList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    servers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Server))), graphql_name='servers')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TopUrlsList(sgqlc.types.Type, PaginatedResults):
    __schema__ = vapi2_schema
    top_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TopUrls))), graphql_name='topUrls')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
vapi2_schema.query_type = NyansaGraphQLQuery
vapi2_schema.mutation_type = None
vapi2_schema.subscription_type = None
