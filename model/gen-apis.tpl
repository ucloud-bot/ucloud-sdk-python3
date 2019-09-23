#!/usr/bin/env bash

# Code is generated by ucloud-model, DO NOT EDIT IT.

ucloud-model sdk apis --lang python3 --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/clients.tpl --output ./ucloud/client.py
ucloud-model sdk apis --lang python3 --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/docs.tpl --output ./docs/services.rst

{{ range $index, $product := (.GetAll | extractUnique "Product") }}
mkdir -p ./ucloud/services/{{ . | lower }}/schemas
touch ./ucloud/services/{{ . | lower }}/__init__.py
touch ./ucloud/services/{{ . | lower }}/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product {{ . }} --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/{{ . | lower }}/schemas/apis.py
ucloud-model sdk apis --lang python3 --product {{ . }} --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/{{ . | lower }}/schemas/models.py
ucloud-model sdk apis --lang python3 --product {{ . }} --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/{{ . | lower }}/client.py
black ucloud/services/{{ . | lower }}
python -m ucloud.services.{{ . | lower }}.client
{{ end }}