import csv
import re
import os

def read_csv(filename):
	csv_file = open('foes.csv', 'r');
	
	csv_reader = csv.reader(csv_file);
	for row in csv_reader:
		print row[1].decode('UTF-8').encode('GBK') ;
	
	csv_file.close();

def is_kept(str):
	list = ["name", "desc", "description"];
	return not(str in list);
	
def export2csv(filename):

	if(not os.path.exists(filename)):
		print filename + "is not found.";

	list = [];
	pattern = re.compile('"(.*?[^\\\\])"')
	
	with open(filename, 'r') as f:
		readstr = f.read();
		list = pattern.findall(readstr)
	
	with open(os.path.splitext(filename)[0] + '.csv', 'wb') as f:
		writer = csv.writer(f)
		for sub in list:
			if(is_kept(sub)): writer.writerow([sub]);

			

export2csv("battles.as");
export2csv("dialogue.as");
export2csv("foes.as");			
export2csv("items.as");
export2csv("foes.as");			
export2csv("items.as");
export2csv("medals.as");			
export2csv("menus.as");
export2csv("npcs.as");			
export2csv("skills.as");
print("complete!");
raw_input();