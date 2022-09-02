# Copyright (c) 2022, nextweb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_site_name

class WebsiteBuilder(Document):
	def before_save(self):

		doc = get_site_name(frappe.local.request.host)
		self.site_name=doc
