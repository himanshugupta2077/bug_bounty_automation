from modules import txt_to_doc_mod

def get_target_info(db, current_directory):
	# creating collection for storing target info
	collec_target_info = db['target_info']

	# defining template for target info
	doc_target_info = {
		'ipv4': '',
		'domain': '',
		'creation_time': '',
	}

	# adding target information into doc_target_info variable
	source = current_directory + "/txts/target_info.txt"
	doc_target_info =  txt_to_doc_mod.txt_to_doc(source, doc_target_info)

	# storing data in collec_target_info
	collec_target_info.insert_one(doc_target_info)

	return collec_target_info
