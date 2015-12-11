from fabric.api import local
import take_book_data as Book
import time

def update():
	Book.login()
	Book.navigate_to_course_search()
	number_of_courses = Book.amount_of_subjects()
	Book.driver.close()
	first_run = int(number_of_courses)/10*10
	second_run = int(number_of_courses)%10
	for index in range(1,first_run,10):
		local('python take_book_data.py %s &' % str(index))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+1))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+2))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+3))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+4))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+5))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+6))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+7))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+8))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+9))
		time.sleep(1000)
	for index in range(first_run+1,second_run+first_run):
		local('python take_book_data.py %s &' % str(index))
		time.sleep(5)

#0- 
#1-Accountancy
#2-Administration & Supervision
#3-African&Black Diaspora Studies
#4-Allied Health Technology
#5-American Sign Language
#6-American Studies
#7-Animation
#8-Anthropology
#9-Applied Brass
#10-Applied Keyboard
#11-Applied Music
#12-Applied Percussion
#13-Applied Professional Studies
#14-Applied Strings
#15-Applied Technology
#16-Applied Voice
#17-Applied Woodwinds
#18-Arabic
#19-Art
#20-Art & Architecture, History of
#21-Arts and Ideas
#22-Asian Studies, Global
#23-Bilingual-Bicultural Education
#24-Biological Sciences
#25-Business Law
#26-Catholic Studies
#27-Chemistry
#28-Chinese
#29-Communication
#30-Communication Studies
#31-Community Service Studies
#32-Comp,Info and Network Security
#33-Comparative Literature
#34-Composition
#35-Computer Graphics & Motion
#36-Computer Science
#37-Core Curriculum Arts and Ideas
#38-Core Curriculum Human Communit
#39-Core Curriculum Scientific Wor
#40-Counseling
#41-Critical Ethnic Studies
#42-Curriculum Studies
#43-Decision Analytics
#44-Degree Completion Major
#45-Design
#46-Digital Cinema
#47-Digital Humanities
#48-Digital Media Arts
#49-E-Commerce Technology
#50-Early Childhood Education
#51-Economics
#52-Educating Adults
#53-Education - General
#54-Elementary Education
#55-English
#56-English Language Academy
#57-Environmental Science
#58-Finance
#59-Focus Area
#60-French
#61-Game Development
#62-Geography
#63-German
#64-Graduate School of Business
#65-Graphic Design
#66-Greek
#67-Health Communication
#68-Health Information Technology
#69-Health Science
#70-History
#71-Honors
#72-Hospitality Leadership
#73-Human Community
#74-Human-Computer Interaction
#75-Illustration
#76-Information Systems
#77-Information Technology
#78-Institute for Professional Dev
#79-Integrative Learning
#80-Interactive and Social Media
#81-Intercultural Communication
#82-Interdisciplinary Comm Studies
#83-Interdisciplinary Studies
#84-International Business
#85-International Studies
#86-Irish Studies
#87-Islamic World Studies
#88-Italian
#89-Japanese
#90-Jazz Studies
#91-Journalism
#92-Latin
#93-LatinAmerican & Latino Studies
#94-Lesbian/Gay/Bisexual/Transgndr
#95-Liberal Learning Seminars
#96-Liberal Studies Program
#97-Liberal Studies in Education
#98-Lifelong Learning
#99-Literacy & Specialized Instruc
#100-Management
#101-Management Information Systems
#102-Marketing
#103-Master of Public Health
#104-Masters in Social Work
#105-Masters of Liberal Studies
#106-Mathematical Sciences
#107-Media Studies
#108-Military Science
#109-Modern Languages
#110-Music Education
#111-Music Ensemble
#112-Musicianship
#113-New Media Studies
#114-Nursing
#115-Organizational Communication
#116-Peace, Justice & Conflict
#117-Performance
#118-Performing Arts Management
#119-Philosophy
#120-Physical Education
#121-Physics
#122-Political Science
#123-Project Management
#124-Psychology
#125-Public Policy Studies
#126-Public Relations & Advertising
#127-Public Services
#128-Real Estate
#129-Refugee/ForcedMigrationStudies
#130-Relational Communication
#131-Religious Studies
#132-Russian
#133-SNL Liberal Studies
#134-Schl for New Learning Graduate
#135-Sci, Tech, Engineering, Math
#136-Scientific World
#137-Secondary Education
#138-Soc/Cult Std Ed Human Dev Grad
#139-Sociology
#140-Socl/Cult Stud Ed/Hum Dev Ugrd
#141-Software Engineering
#142-Sound Recording Technology
#143-Spanish
#144-Study Abroad Program
#145-Sustainable Urban Development
#146-TEACH Program
#147-Teaching and Learning
#148-Telecommunications
#149-Television Production
#150-Theatre Studies
#151-Theatre Technology
#152-University Internship Program
#153-Visual Effects
#154-Women's and Gender Studies
#155-World Language Education
#156-Writing Rhetoric and Discourse