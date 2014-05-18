polycircles
===========

Polycircles: WGS84 Circle approximations using polygons.

[![Build Status](https://travis-ci.org/adamatan/polycircles.svg?branch=master)](https://travis-ci.org/adamatan/polycircles) [![Latest Version](https://pypip.in/version/polycircles/badge.png)](https://pypi.python.org/pypi/polycircles/) 

Approximate a circle using a 36-vertices polygon:

	>>> from polycircles import polycircles
	>>> polycircle = polycircles.Polycircle(latitude = 32.074322, longitude=34.792081, radius=100, number_of_vertices=36)
	>>> polycircle.to_lat_lon()
	((32.075223809870174, 34.792081), (32.075210109219384, 34.79226491831068), (32.07516942356622, 34.792443248196115), (32.07510298915787, 34.792610571051924), (32.075012824622526, 34.79276180275308), (32.074901669628204, 34.792892348145145), (32.07477290163153, 34.792998240672475), (32.07463043324713, 34.793076262899916), (32.074478593357114, 34.79312404426628), (32.07432199557388, 34.79314013310001), (32.0741653980537, 34.79312404071046), (32.07401355892112, 34.793076256217155), (32.07387109169717, 34.79299823166882), (32.073742325123995, 34.792892337906565), (32.073631171644536, 34.79276179251449), (32.07354100853271, 34.79261056204826), (32.07347457528479, 34.792443241513354), (32.07343389038906, 34.79226491475485), (32.07342019000132, 34.792081), (32.07343389038906, 34.791897085245154), (32.07347457528479, 34.79171875848665), (32.07354100853271, 34.791551437951746), (32.073631171644536, 34.791400207485516), (32.073742325123995, 34.79126966209344), (32.07387109169717, 34.79116376833119), (32.07401355892112, 34.79108574378285), (32.0741653980537, 34.79103795928955), (32.07432199557388, 34.791021866899996), (32.074478593357114, 34.79103795573373), (32.07463043324713, 34.79108573710009), (32.07477290163153, 34.79116375932753), (32.074901669628204, 34.79126965185486), (32.075012824622526, 34.79140019724693), (32.07510298915787, 34.79155142894808), (32.07516942356622, 34.79171875180389), (32.075210109219384, 34.79189708168933))
