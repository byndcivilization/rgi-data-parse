#!/usr/bin/python
"""Parses and loads RGI questions from excel into MongoDB"""


from xlrd import open_workbook
from sys import argv
from pilot_parser import parse
from pymongo import MongoClient
import json
from pprint import pprint
# from utils import write_json



def main(args):
    """Main body"""
    args_len = len(args)

    class SetEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, set):
                return list(obj)
                return json.JSONEncoder.default(self, obj)
 

    # set source excel and destination json files
    if args_len == 1:
        src = args[0] + '.xlsx'
        dest = args[0] + '.json'
    elif args_len == 2:
        src = args[0] + '.xlsx'
        dest = args[1] + '.json'
    else:
        print 'you must enter valid source and destination file names. If you enter a single \
        argument, that will be taken as both source and desitnation name. Please limit input \
        to two arguments.'
        exit()

    # Error handling for non-existing files
    try:
        workbook = open_workbook(src)
    except IOError:
        print 'File does not exist. Please give a valid source file'
        exit()

    data = []

    # get sheets names
    sheet_names = workbook.sheet_names()

    parse(sheet_names[1], workbook.sheet_by_name(sheet_names[1]), data)

    countries_data = [
        {'country': 'Afghanistan', 'country_ID': 'AFG', 'iso2': 'AF'},
        # {'country': 'Aland Islands', 'country_ID': 'ALA', 'iso2': 'AX'},
        {'country': 'Albania', 'country_ID': 'ALB', 'iso2': 'AL'},
        {'country': 'Algeria', 'country_ID': 'DZA', 'iso2': 'DZ'},
        # {'country': 'American Samoa', 'country_ID': 'ASM', 'iso2': 'AS'},
        # {'country': 'Andorra', 'country_ID': 'AND', 'iso2': 'AD'},
        {'country': 'Angola', 'country_ID': 'AGO', 'iso2': 'AO'},
        # {'country': 'Anguilla', 'country_ID': 'AIA', 'iso2': 'AI'},
        # {'country': 'Antarctica', 'country_ID': 'ATA', 'iso2': 'AQ'},
        {'country': 'Antigua and Barbuda', 'country_ID': 'ATG', 'iso2': 'AG'},
        {'country': 'Argentina', 'country_ID': 'ARG', 'iso2': 'AR'},
        {'country': 'Armenia', 'country_ID': 'ARM', 'iso2': 'AM'},
        {'country': 'Aruba', 'country_ID': 'ABW', 'iso2': 'AW'},
        {'country': 'Australia', 'country_ID': 'AUS', 'iso2': 'AU'},
        {'country': 'Austria', 'country_ID': 'AUT', 'iso2': 'AT'},
        {'country': 'Azerbaijan', 'country_ID': 'AZE', 'iso2': 'AZ'},
        {'country': 'Bahamas', 'country_ID': 'BHS', 'iso2': 'BS'},
        {'country': 'Bahrain', 'country_ID': 'BHR', 'iso2': 'BH'},
        {'country': 'Bangladesh', 'country_ID': 'BGD', 'iso2': 'BD'},
        {'country': 'Barbados', 'country_ID': 'BRB', 'iso2': 'BB'},
        {'country': 'Belarus', 'country_ID': 'BLR', 'iso2': 'BY'},
        {'country': 'Belgium', 'country_ID': 'BEL', 'iso2': 'BE'},
        {'country': 'Belize', 'country_ID': 'BLZ', 'iso2': 'BZ'},
        {'country': 'Benin', 'country_ID': 'BEN', 'iso2': 'BJ'},
        {'country': 'Bermuda', 'country_ID': 'BMU', 'iso2': 'BM'},
        {'country': 'Bhutan', 'country_ID': 'BTN', 'iso2': 'BT'},
        {'country': 'Bolivia, Plurinational State of', 'country_ID': 'BOL', 'iso2': 'BO'},
        # {'country': 'Bonaire, Sint Eustatius and Saba', 'country_ID': 'BES', 'iso2': 'BQ'},
        {'country': 'Bosnia and Herzegovina', 'country_ID': 'BIH', 'iso2': 'BA'},
        {'country': 'Botswana', 'country_ID': 'BWA', 'iso2': 'BW'},
        # {'country': 'Bouvet Island', 'country_ID': 'BVT', 'iso2': 'BV'},
        {'country': 'Brazil', 'country_ID': 'BRA', 'iso2': 'BR'},
        # {'country': 'British Indian Ocean Territory', 'country_ID': 'IOT', 'iso2': 'IO'},
        {'country': 'Brunei Darussalam', 'country_ID': 'BRN', 'iso2': 'BN'},
        {'country': 'Bulgaria', 'country_ID': 'BGR', 'iso2': 'BG'},
        {'country': 'Burkina Faso', 'country_ID': 'BFA', 'iso2': 'BF'},
        {'country': 'Burundi', 'country_ID': 'BDI', 'iso2': 'BI'},
        {'country': 'Cambodia', 'country_ID': 'KHM', 'iso2': 'KH'},
        {'country': 'Cameroon', 'country_ID': 'CMR', 'iso2': 'CM'},
        {'country': 'Canada', 'country_ID': 'CAN', 'iso2': 'CA'},
        {'country': 'Cape Verde', 'country_ID': 'CPV', 'iso2': 'CV'},
        {'country': 'Cayman Islands', 'country_ID': 'CYM', 'iso2': 'KY'},
        {'country': 'Central African Republic', 'country_ID': 'CAF', 'iso2': 'CF'},
        {'country': 'Chad', 'country_ID': 'TCD', 'iso2': 'TD'},
        {'country': 'Chile', 'country_ID': 'CHL', 'iso2': 'CL'},
        {'country': 'China', 'country_ID': 'CHN', 'iso2': 'CN'},
        # {'country': 'Christmas Island', 'country_ID': 'CXR', 'iso2': 'CX'},
        # {'country': 'Cocos (Keeling) Islands', 'country_ID': 'CCK', 'iso2': 'CC'},
        {'country': 'Colombia', 'country_ID': 'COL', 'iso2': 'CO'},
        {'country': 'Comoros', 'country_ID': 'COM', 'iso2': 'KM'},
        {'country': 'Congo', 'country_ID': 'COG', 'iso2': 'CG'},
        {'country': 'Congo, The Democratic Republic of the', 'country_ID': 'COD', 'iso2': 'CD'},
        # {'country': 'Cook Islands', 'country_ID': 'COK', 'iso2': 'CK'},
        {'country': 'Costa Rica', 'country_ID': 'CRI', 'iso2': 'CR'},
        {'country': 'Cote d\'Ivoire', 'country_ID': 'CIV', 'iso2': 'CI'},
        {'country': 'Croatia', 'country_ID': 'HRV', 'iso2': 'HR'},
        {'country': 'Cuba', 'country_ID': 'CUB', 'iso2': 'CU'},
        # {'country': 'Curacao', 'country_ID': 'CUW', 'iso2': 'CW'},
        {'country': 'Cyprus', 'country_ID': 'CYP', 'iso2': 'CY'},
        {'country': 'Czech Republic', 'country_ID': 'CZE', 'iso2': 'CZ'},
        {'country': 'Denmark', 'country_ID': 'DNK', 'iso2': 'DK'},
        {'country': 'Djibouti', 'country_ID': 'DJI', 'iso2': 'DJ'},
        {'country': 'Dominica', 'country_ID': 'DMA', 'iso2': 'DM'},
        {'country': 'Dominican Republic', 'country_ID': 'DOM', 'iso2': 'DO'},
        {'country': 'Ecuador', 'country_ID': 'ECU', 'iso2': 'EC'},
        {'country': 'Egypt', 'country_ID': 'EGY', 'iso2': 'EG'},
        {'country': 'El Salvador', 'country_ID': 'SLV', 'iso2': 'SV'},
        {'country': 'Equatorial Guinea', 'country_ID': 'GNQ', 'iso2': 'GQ'},
        {'country': 'Eritrea', 'country_ID': 'ERI', 'iso2': 'ER'},
        {'country': 'Estonia', 'country_ID': 'EST', 'iso2': 'EE'},
        {'country': 'Ethiopia', 'country_ID': 'ETH', 'iso2': 'ET'},
        # {'country': 'Falkland Islands (Malvinas)', 'country_ID': 'FLK', 'iso2': 'FK'},
        # {'country': 'Faroe Islands', 'country_ID': 'FRO', 'iso2': 'FO'},
        {'country': 'Fiji', 'country_ID': 'FJI', 'iso2': 'FJ'},
        {'country': 'Finland', 'country_ID': 'FIN', 'iso2': 'FI'},
        {'country': 'France', 'country_ID': 'FRA', 'iso2': 'FR'},
        # {'country': 'French Guiana', 'country_ID': 'GUF', 'iso2': 'GF'},
        # {'country': 'French Polynesia', 'country_ID': 'PYF', 'iso2': 'PF'},
        # {'country': 'French Southern Territories', 'country_ID': 'ATF', 'iso2': 'TF'},
        {'country': 'Gabon', 'country_ID': 'GAB', 'iso2': 'GA'},
        {'country': 'Gambia', 'country_ID': 'GMB', 'iso2': 'GM'},
        {'country': 'Georgia', 'country_ID': 'GEO', 'iso2': 'GE'},
        {'country': 'Germany', 'country_ID': 'DEU', 'iso2': 'DE'},
        {'country': 'Ghana', 'country_ID': 'GHA', 'iso2': 'GH'},
        # {'country': 'Gibraltar', 'country_ID': 'GIB', 'iso2': 'GI'},
        {'country': 'Greece', 'country_ID': 'GRC', 'iso2': 'GR'},
        {'country': 'Greenland', 'country_ID': 'GRL', 'iso2': 'GL'},
        {'country': 'Grenada', 'country_ID': 'GRD', 'iso2': 'GD'},
        # {'country': 'Guadeloupe', 'country_ID': 'GLP', 'iso2': 'GP'},
        {'country': 'Guam', 'country_ID': 'GUM', 'iso2': 'GU'},
        {'country': 'Guatemala', 'country_ID': 'GTM', 'iso2': 'GT'},
        # {'country': 'Guernsey', 'country_ID': 'GGY', 'iso2': 'GG'},
        {'country': 'Guinea', 'country_ID': 'GIN', 'iso2': 'GN'},
        {'country': 'Guinea-Bissau', 'country_ID': 'GNB', 'iso2': 'GW'},
        {'country': 'Guyana', 'country_ID': 'GUY', 'iso2': 'GY'},
        {'country': 'Haiti', 'country_ID': 'HTI', 'iso2': 'HT'},
        # {'country': 'Heard Island and McDonald Islands', 'country_ID': 'HMD', 'iso2': 'HM'},
        # {'country': 'Holy See (Vatican City State)', 'country_ID': 'VAT', 'iso2': 'VA'},
        {'country': 'Honduras', 'country_ID': 'HND', 'iso2': 'HN'},
        {'country': 'Hong Kong', 'country_ID': 'HKG', 'iso2': 'HK'},
        {'country': 'Hungary', 'country_ID': 'HUN', 'iso2': 'HU'},
        {'country': 'Iceland', 'country_ID': 'ISL', 'iso2': 'IS'},
        {'country': 'India', 'country_ID': 'IND', 'iso2': 'IN'},
        {'country': 'Indonesia', 'country_ID': 'IDN', 'iso2': 'ID'},
        {'country': 'Iran, Islamic Republic of', 'country_ID': 'IRN', 'iso2': 'IR'},
        {'country': 'Iraq', 'country_ID': 'IRQ', 'iso2': 'IQ'},
        {'country': 'Ireland', 'country_ID': 'IRL', 'iso2': 'IE'},
        # {'country': 'Isle of Man', 'country_ID': 'IMN', 'iso2': 'IM'},
        {'country': 'Israel', 'country_ID': 'ISR', 'iso2': 'IL'},
        {'country': 'Italy', 'country_ID': 'ITA', 'iso2': 'IT'},
        {'country': 'Jamaica', 'country_ID': 'JAM', 'iso2': 'JM'},
        {'country': 'Japan', 'country_ID': 'JPN', 'iso2': 'JP'},
        # {'country': 'Jersey', 'country_ID': 'JEY', 'iso2': 'JE'},
        {'country': 'Jordan', 'country_ID': 'JOR', 'iso2': 'JO'},
        {'country': 'Kazakhstan', 'country_ID': 'KAZ', 'iso2': 'KZ'},
        {'country': 'Kenya', 'country_ID': 'KEN', 'iso2': 'KE'},
        {'country': 'Kiribati', 'country_ID': 'KIR', 'iso2': 'KI'},
        {'country': 'DPRK Korea', 'country_ID': 'PRK', 'iso2': 'KP'},
        {'country': 'Republic of Korea', 'country_ID': 'KOR', 'iso2': 'KR'},
        {'country': 'Kuwait', 'country_ID': 'KWT', 'iso2': 'KW'},
        {'country': 'Kyrgyzstan', 'country_ID': 'KGZ', 'iso2': 'KG'},
        {'country': 'Lao Peoples Democratic Republic', 'country_ID': 'LAO', 'iso2': 'LA'},
        {'country': 'Latvia', 'country_ID': 'LVA', 'iso2': 'LV'},
        {'country': 'Lebanon', 'country_ID': 'LBN', 'iso2': 'LB'},
        {'country': 'Lesotho', 'country_ID': 'LSO', 'iso2': 'LS'},
        {'country': 'Liberia', 'country_ID': 'LBR', 'iso2': 'LR'},
        {'country': 'Libya', 'country_ID': 'LBY', 'iso2': 'LY'},
        {'country': 'Liechtenstein', 'country_ID': 'LIE', 'iso2': 'LI'},
        {'country': 'Lithuania', 'country_ID': 'LTU', 'iso2': 'LT'},
        {'country': 'Luxembourg', 'country_ID': 'LUX', 'iso2': 'LU'},
        # {'country': 'Macao', 'country_ID': 'MAC', 'iso2': 'MO'},
        {'country': 'Macedonia, Republic of', 'country_ID': 'MKD', 'iso2': 'MK'},
        {'country': 'Madagascar', 'country_ID': 'MDG', 'iso2': 'MG'},
        {'country': 'Malawi', 'country_ID': 'MWI', 'iso2': 'MW'},
        {'country': 'Malaysia', 'country_ID': 'MYS', 'iso2': 'MY'},
        # {'country': 'Maldives', 'country_ID': 'MDV', 'iso2': 'MV'},
        {'country': 'Mali', 'country_ID': 'MLI', 'iso2': 'ML'},
        # {'country': 'Malta', 'country_ID': 'MLT', 'iso2': 'MT'},
        # {'country': 'Marshall Islands', 'country_ID': 'MHL', 'iso2': 'MH'},
        # {'country': 'Martinique', 'country_ID': 'MTQ', 'iso2': 'MQ'},
        {'country': 'Mauritania', 'country_ID': 'MRT', 'iso2': 'MR'},
        # {'country': 'Mauritius', 'country_ID': 'MUS', 'iso2': 'MU'},
        # {'country': 'Mayotte', 'country_ID': 'MYT', 'iso2': 'YT'},
        {'country': 'Mexico', 'country_ID': 'MEX', 'iso2': 'MX'},
        # {'country': 'Micronesia, Federated States of', 'country_ID': 'FSM', 'iso2': 'FM'},
        {'country': 'Moldova, Republic of', 'country_ID': 'MDA', 'iso2': 'MD'},
        # {'country': 'Monaco', 'country_ID': 'MCO', 'iso2': 'MC'},
        {'country': 'Mongolia', 'country_ID': 'MNG', 'iso2': 'MN'},
        {'country': 'Montenegro', 'country_ID': 'MNE', 'iso2': 'ME'},
        # {'country': 'Montserrat', 'country_ID': 'MSR', 'iso2': 'MS'},
        {'country': 'Morocco', 'country_ID': 'MAR', 'iso2': 'MA'},
        {'country': 'Mozambique', 'country_ID': 'MOZ', 'iso2': 'MZ'},
        {'country': 'Myanmar', 'country_ID': 'MMR', 'iso2': 'MM'},
        {'country': 'Namibia', 'country_ID': 'NAM', 'iso2': 'NA'},
        # {'country': 'Nauru', 'country_ID': 'NRU', 'iso2': 'NR'},
        {'country': 'Nepal', 'country_ID': 'NPL', 'iso2': 'NP'},
        {'country': 'Netherlands', 'country_ID': 'NLD', 'iso2': 'NL'},
        # {'country': 'New Caledonia', 'country_ID': 'NCL', 'iso2': 'NC'},
        {'country': 'New Zealand', 'country_ID': 'NZL', 'iso2': 'NZ'},
        {'country': 'Nicaragua', 'country_ID': 'NIC', 'iso2': 'NI'},
        {'country': 'Niger', 'country_ID': 'NER', 'iso2': 'NE'},
        {'country': 'Nigeria', 'country_ID': 'NGA', 'iso2': 'NG'},
        # {'country': 'Niue', 'country_ID': 'NIU', 'iso2': 'NU'},
        # {'country': 'Norfolk Island', 'country_ID': 'NFK', 'iso2': 'NF'},
        # {'country': 'Northern Mariana Islands', 'country_ID': 'MNP', 'iso2': 'MP'},
        {'country': 'Norway', 'country_ID': 'NOR', 'iso2': 'NO'},
        {'country': 'Oman', 'country_ID': 'OMN', 'iso2': 'OM'},
        {'country': 'Pakistan', 'country_ID': 'PAK', 'iso2': 'PK'},
        # {'country': 'Palau', 'country_ID': 'PLW', 'iso2': 'PW'},
        {'country': 'Palestine, State of', 'country_ID': 'PSE', 'iso2': 'PS'},
        {'country': 'Panama', 'country_ID': 'PAN', 'iso2': 'PA'},
        {'country': 'Papua New Guinea', 'country_ID': 'PNG', 'iso2': 'PG'},
        {'country': 'Paraguay', 'country_ID': 'PRY', 'iso2': 'PY'},
        {'country': 'Peru', 'country_ID': 'PER', 'iso2': 'PE'},
        {'country': 'Philippines', 'country_ID': 'PHL', 'iso2': 'PH'},
        # {'country': 'Pitcairn', 'country_ID': 'PCN', 'iso2': 'PN'},
        {'country': 'Poland', 'country_ID': 'POL', 'iso2': 'PL'},
        {'country': 'Portugal', 'country_ID': 'PRT', 'iso2': 'PT'},
        {'country': 'Puerto Rico', 'country_ID': 'PRI', 'iso2': 'PR'},
        {'country': 'Qatar', 'country_ID': 'QAT', 'iso2': 'QA'},
        # {'country': 'Reunion', 'country_ID': 'REU', 'iso2': 'RE'},
        {'country': 'Romania', 'country_ID': 'ROU', 'iso2': 'RO'},
        {'country': 'Russian Federation', 'country_ID': 'RUS', 'iso2': 'RU'},
        {'country': 'Rwanda', 'country_ID': 'RWA', 'iso2': 'RW'},
        # {'country': 'Saint Barthelemy', 'country_ID': 'BLM', 'iso2': 'BL'},
        # {'country': 'Saint Helena, Ascension and Tristan da Cunha', 'country_ID': 'SHN', 'iso2': 'SH'},
        # {'country': 'Saint Kitts and Nevis', 'country_ID': 'KNA', 'iso2': 'KN'},
        # {'country': 'Saint Lucia', 'country_ID': 'LCA', 'iso2': 'LC'},
        # {'country': 'Saint Martin (French part)', 'country_ID': 'MAF', 'iso2': 'MF'},
        # {'country': 'Saint Pierre and Miquelon', 'country_ID': 'SPM', 'iso2': 'PM'},
        # {'country': 'Saint Vincent and the Grenadines', 'country_ID': 'VCT', 'iso2': 'VC'},
        # {'country': 'Samoa', 'country_ID': 'WSM', 'iso2': 'WS'},
        # {'country': 'San Marino', 'country_ID': 'SMR', 'iso2': 'SM'},
        {'country': 'Sao Tome and Principe', 'country_ID': 'STP', 'iso2': 'ST'},
        {'country': 'Saudi Arabia', 'country_ID': 'SAU', 'iso2': 'SA'},
        {'country': 'Senegal', 'country_ID': 'SEN', 'iso2': 'SN'},
        {'country': 'Serbia', 'country_ID': 'SRB', 'iso2': 'RS'},
        {'country': 'Seychelles', 'country_ID': 'SYC', 'iso2': 'SC'},
        {'country': 'Sierra Leone', 'country_ID': 'SLE', 'iso2': 'SL'},
        {'country': 'Singapore', 'country_ID': 'SGP', 'iso2': 'SG'},
        # {'country': 'Sint Maarten (Dutch part)', 'country_ID': 'SXM', 'iso2': 'SX'},
        {'country': 'Slovakia', 'country_ID': 'SVK', 'iso2': 'SK'},
        {'country': 'Slovenia', 'country_ID': 'SVN', 'iso2': 'SI'},
        # {'country': 'Solomon Islands', 'country_ID': 'SLB', 'iso2': 'SB'},
        {'country': 'Somalia', 'country_ID': 'SOM', 'iso2': 'SO'},
        {'country': 'South Africa', 'country_ID': 'ZAF', 'iso2': 'ZA'},
        # {'country': 'South Georgia and the South Sandwich Islands', 'country_ID': 'SGS', 'iso2': 'GS'},
        {'country': 'Spain', 'country_ID': 'ESP', 'iso2': 'ES'},
        {'country': 'Sri Lanka', 'country_ID': 'LKA', 'iso2': 'LK'},
        {'country': 'Sudan', 'country_ID': 'SDN', 'iso2': 'SD'},
        {'country': 'Suriname', 'country_ID': 'SUR', 'iso2': 'SR'},
        {'country': 'South Sudan', 'country_ID': 'SSD', 'iso2': 'SS'},
        # {'country': 'Svalbard and Jan Mayen', 'country_ID': 'SJM', 'iso2': 'SJ'},
        {'country': 'Swaziland', 'country_ID': 'SWZ', 'iso2': 'SZ'},
        {'country': 'Sweden', 'country_ID': 'SWE', 'iso2': 'SE'},
        {'country': 'Switzerland', 'country_ID': 'CHE', 'iso2': 'CH'},
        {'country': 'Syrian Arab Republic', 'country_ID': 'SYR', 'iso2': 'SY'},
        {'country': 'Taiwan, Province of China', 'country_ID': 'TWN', 'iso2': 'TW'},
        {'country': 'Tajikistan', 'country_ID': 'TJK', 'iso2': 'TJ'},
        {'country': 'Tanzania, United Republic of', 'country_ID': 'TZA', 'iso2': 'TZ'},
        {'country': 'Thailand', 'country_ID': 'THA', 'iso2': 'TH'},
        {'country': 'Timor-Leste', 'country_ID': 'TLS', 'iso2': 'TL'},
        {'country': 'Togo', 'country_ID': 'TGO', 'iso2': 'TG'},
        # {'country': 'Tokelau', 'country_ID': 'TKL', 'iso2': 'TK'},
        # {'country': 'Tonga', 'country_ID': 'TON', 'iso2': 'TO'},
        {'country': 'Trinidad and Tobago', 'country_ID': 'TTO', 'iso2': 'TT'},
        {'country': 'Tunisia', 'country_ID': 'TUN', 'iso2': 'TN'},
        {'country': 'Turkey', 'country_ID': 'TUR', 'iso2': 'TR'},
        {'country': 'Turkmenistan', 'country_ID': 'TKM', 'iso2': 'TM'},
        # {'country': 'Turks and Caicos Islands', 'country_ID': 'TCA', 'iso2': 'TC'},
        # {'country': 'Tuvalu', 'country_ID': 'TUV', 'iso2': 'TV'},
        {'country': 'Uganda', 'country_ID': 'UGA', 'iso2': 'UG'},
        {'country': 'Ukraine', 'country_ID': 'UKR', 'iso2': 'UA'},
        {'country': 'United Arab Emirates', 'country_ID': 'ARE', 'iso2': 'AE'},
        {'country': 'United Kingdom', 'country_ID': 'GBR', 'iso2': 'GB'},
        {'country': 'United States', 'country_ID': 'USA', 'iso2': 'US'},
        # {'country': 'United States Minor Outlying Islands', 'country_ID': 'UMI', 'iso2': 'UM'},
        {'country': 'Uruguay', 'country_ID': 'URY', 'iso2': 'UY'},
        {'country': 'Uzbekistan', 'country_ID': 'UZB', 'iso2': 'UZ'},
        # {'country': 'Vanuatu', 'country_ID': 'VUT', 'iso2': 'VU'},
        {'country': 'Venezuela, Bolivarian Republic of', 'country_ID': 'VEN', 'iso2': 'VE'},
        {'country': 'Viet Nam', 'country_ID': 'VNM', 'iso2': 'VN'},
        # {'country': 'Virgin Islands, British', 'country_ID': 'VGB', 'iso2': 'VG'},
        # {'country': 'Virgin Islands, U.S.', 'country_ID': 'VIR', 'iso2': 'VI'},
        # {'country': 'Wallis and Futuna', 'country_ID': 'WLF', 'iso2': 'WF'},
        # {'country': 'Western Sahara', 'country_ID': 'ESH', 'iso2': 'EH'},
        {'country': 'Yemen', 'country_ID': 'YEM', 'iso2': 'YE'},
        {'country': 'Zambia', 'country_ID': 'ZMB', 'iso2': 'ZM'},
        {'country': 'Zimbabwe', 'country_ID': 'ZWE', 'iso2': 'ZW'}
    ]



    env_list = ["1: Remote", "2: Local"]
    try:
        env_pick = input("Select the destination environment: " + ' '.join(env_list) + "\n")
    except NameError:
        print 'You must pick 1 or 2'
        exit()
    if env_pick < 1 or env_pick > 2:
        print 'You must pick 1 or 2'
        exit()
    elif env_pick == 1:
        environment = 'remote'
    elif env_pick == 2:
        environment = 'local'

    if environment == 'remote':
        username = raw_input('Enter your MongoDB username [empty for no db]: ')
        if username != '':
            password = raw_input('Enter your MongoDB password: ')
            if password == '':
                print 'You must enter a password'
                exit()
        else:
            print 'You must enter a username'
            exit()

    database = raw_input('Enter Mongo database you want to insert into: ')
    if database == '':
        print 'You must enter a database'
        exit()
    
    
    # Make db connection
    collection_name = 'questions'
    if environment == 'local':
        mongo_url = 'mongodb://localhost/' + database
        client = MongoClient('localhost', 27017)
        mongo_db = client[database]
    elif environment == 'remote':
        mongo_url = 'mongodb://' + username + ':' + password + '@c726.candidate.19.mongolayer.com:10726/' + database
        client = MongoClient(mongo_url)
        mongo_db = client[database]
        try:
            mongo_db.authenticate(username, password)
            print "Authenticated Mongo connection."
        except:
            print "Wrong username or password!"
            exit()

    collection = mongo_db[collection_name]
    country_collection = mongo_db['countries']
    if country_collection.find({}).count() == 0:
        country_collection.insert(countries_data)
    if collection.find({}).count() == 0:
        collection.insert(data)
        print str(len(data)) + " documents inserted into " + collection_name + \
        " collection in the "+ database + " database."
    else:
        print 'Data exists'
        exit()


    # # print data
    # # write out archive of update into archive folder
    print_out = open('./' + dest, 'w')
    # # print_out.write(json.dumps(data, cls=SetEncoder, indent=4, separators=(',', ':')))
    print_out.write(json.dumps(data, cls=SetEncoder, separators=(',', ':')))
    print 'data written into ' + dest + ' file'
    print_out.close()


if __name__ == '__main__':
    main(argv[1:])
