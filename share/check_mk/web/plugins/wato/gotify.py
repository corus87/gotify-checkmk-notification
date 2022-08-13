#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# Gotify notification based on https://exchange.checkmk.com/p/telegram-notifications.
# SPDX-License-Identifier: GPL-2.0-onl

from cmk.gui.valuespec import Dictionary, TextAscii
from cmk.gui.plugins.wato import notification_parameter_registry, NotificationParameter

@notification_parameter_registry.register
class NotificationParameterGortify(NotificationParameter):
    @property
    def ident(self):
        return "gotify"
    @property
    def spec(self):
        return Dictionary(
            title=_("Create notification with the following parameters"),
            required_keys=["url", "token", "priority", "gotify_title"],
            elements=[
                (
                    "url",
                    TextAscii(
                        title=_("url"),
                        help=_("URL for of Gotify Server"),
                        size=46,
                        allow_empty=False,
                    ),
                ),
                (
                    "token",
                    TextAscii(
                        title=_("token"),
                        help=_("Token to send notifications"),
                        size=24,
                        allow_empty=False,
                    ),
                ),
                (
                    "priority",
                    Integer(
                        title=_("Priority"),
                        help=_("Message priority. The Android client classifies messages by High (7), Normal (4-7), Low (1-3) and Minimum priority (1)."),
                        size=24,
                        minvalue=1,
                        maxvalue=7,
                        default_value=4,
                    ),
                ),
                (
                    "gotify_title",
                    TextAscii(
                        title=_("Gotify Title"),
                        help=_("Title of Gotify notification"),
                        size=24,
                        default_value="CheckMK"
                    ),
                ),
            ],
        )

