def get_PVT(gprmc_sentence: str):
	"""
		get position, velocity and time data from GPRMC sentence.
		Return a tuple containing: validity of received GPRMC sentence,
		GPS peovided date, GPS provided time, latitude, longitude and
		velocity
	"""
	sentence_segments = gprmc_sentence.split(',')
	isValid = False
	gps_date = ''
	gps_time = ''
	latitude = ''
	longitude = ''
	velocity = ''
	try:
		if(sentence_segments[2] == 'A'):
			isValid = True
			gps_date = (sentence_segments[9])[:2] + '/' + \
			(sentence_segments[9])[2:4] + '/' + (sentence_segments[9])[4:]
			gps_time = (sentence_segments[1])[:2] + ':' + \
			(sentence_segments[1])[2:4] + ':' + (sentence_segments[1])[4:] + 'GMT'
			latitude = '{:.5f}'.format(float((sentence_segments[3])[:2]) + \
			float((sentence_segments[3])[2:]) / float(60)) + sentence_segments[4]
			longitude = '{:.5f}'.format(float((sentence_segments[5])[:3]) + \
			float((sentence_segments[5])[3:]) / float(60)) + sentence_segments[6]
			velocity = sentence_segments[7] + 'm/s'
		elif(sentence_segments[2] == 'V'):
			isValid = False
			gps_date = (sentence_segments[9])[:2] + '/' + (sentence_segments[9])[2:4] + \
			'/' + (sentence_segments[9])[4:] if sentence_segments[9] else ''
			gps_time = (sentence_segments[1])[:2] + ':' + (sentence_segments[1])[2:4] + \
			':' + (sentence_segments[1])[4:] + 'GMT' if sentence_segments[1] else ''
			latitude = '{:.5f}'.format(float((sentence_segments[3])[:2]) + \
			float((sentence_segments[3])[2:]) / float(60)) + sentence_segments[4] if sentence_segments[3] else ''
			longitude = '{:.5f}'.format(float((sentence_segments[5])[:3]) + \
			float((sentence_segments[5])[3:]) / float(60)) + sentence_segments[6] if sentence_segments[5] else ''
			velocity = sentence_segments[7] + 'm/s' if sentence_segments[7] else ''

	except Exception as e:
		print(e)
		
	return (isValid, gps_date, gps_time, latitude, longitude, velocity)
			

