OPENSTACK CORS
===============

Makes it easier to add CORS support to openstack all api components

About Cross-Origin Resource Sharing (CORS)
------------------------------------------

- http://en.wikipedia.org/wiki/Cross-origin_resource_sharing
- http://www.w3.org/TR/cors/

Installing
----------

```
python setup.py install
```

Using
-----

#### Cinder

1. vim /etc/cinder/api-paste.ini
```
[filter:support_options]
paste.filter_factory = openstack_cors:CorsMixin.factory

[composite:openstack_volume_api_v1]
use = call:cinder.api.middleware.auth:pipeline_factory
noauth = support_options request_id faultwrap sizelimit osprofiler noauth apiv1
keystone = support_options request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv1
keystone_nolimit = support_options request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv1

[composite:openstack_volume_api_v2]
use = call:cinder.api.middleware.auth:pipeline_factory
noauth = support_options request_id faultwrap sizelimit osprofiler noauth apiv2
keystone = support_options request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv2
keystone_nolimit = support_options request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv2
```

2. restart cinder-api
```
systemctl restart openstack-cinder-api
```

#### Ceilometer

1. vim /etc/ceilometer/api_paste.ini
```
[pipeline:main]
pipeline = support_options uthtoken api-server

[filter:support_options]
paste.filter_factory = openstack_cors:CorsMixin.factory
```

2. restart ceilometer-api
```
systemctl restart openstack-ceilometer-api
```

Keystone、Glance、Neutron、Nova has similar configuration.
