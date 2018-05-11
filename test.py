# coding: utf-8


# based on 100 words per paragraph
sample_paragraph = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, hjyyj. \n\n"
get_essay = ""

def paragraph_generator(num_paras):
	essay_template = "test"

	if num_paras > 0:
		for num in range(int(num_paras)):
		# essay_template = sample_paragraph * num_paras
		# print(essay_template)
			# holds final essay
			essay_template = essay_template + sample_paragraph
	else:
		print("Number of paragraphs cannot be less than 1.")
	print(essay_template)
	paragraph_generator.get_essay = essay_template
	# print(get_essay)

def word_count_to_paragraph(word_count):
	# divide word count by 100 (100 words a paragraph)
	paragraph_count = word_count/(100)
	# word count exists and less than a paragraph
	if paragraph_count < 1 and (float(word_count) < 100):
		# set the paragraph count to one paragraph
		paragraph_count = 1
		paragraph_generator(paragraph_count)
	else:
		print(str(paragraph_count))
		paragraph_generator(paragraph_count)
	print("Paragraph count = ", paragraph_count)

# accept integer user input
word_count = float(input("How many words does the essay need to be?"))
word_count_to_paragraph(word_count)
print(paragraph_generator.get_essay)