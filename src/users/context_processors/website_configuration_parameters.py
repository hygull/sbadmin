from .change import WEBSITE_TOP_LEFT_NAME, WEBSITE_FOOTER_NAME
from datetime import datetime


def website_configuration_parameters(request):
	conf_params = {
		"WEBSITE_FOOTER_NAME": WEBSITE_FOOTER_NAME,
		"WEBSITE_TOP_LEFT_NAME": WEBSITE_TOP_LEFT_NAME,
		"CURRENT_YEAR": datetime.now().year
	}

	return conf_params