# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-节点管理(BlueKing-BK-NODEMAN) available.
Copyright (C) 2017-2022 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
# Generated by Django 2.2.8 on 2021-04-10 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("node_man", "0039_merge_20210409_1713"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="processstatus",
            unique_together={("bk_host_id", "listen_port")},
        ),
    ]
