from tkinter import *
import tkinter.ttk as ttk
import analize as an

class App:
	def __init__(self):
		self.screen = Tk()

		lableStyle = ttk.Style()
		lableStyle.configure("Standard.Label", background="#445663", font=("courier", 15, "bold"), foreground ="red")


		# ---------------- Basic config ----------------------
		self.screen.title("Analizer")
		self.screen.config(bg="black")

		# Menu for More 
		self.main_frame = Frame(self.screen,)
		self.main_frame.pack()

		# Menu for excel configue nad chart
		self.left_frame = Frame(self.main_frame)
		self.left_frame.grid(row = 0, column = 0)

		self.widget_frame = ttk.LabelFrame(self.left_frame, text = "TEST TEXT", style = "Standard.Label")
		self.widget_frame.grid(row = 0, column = 0, padx = 10, pady = (0, 10))

		# Entry fields
		self.file_name = self.createEntry(self.widget_frame, "Excel Name", 0, 0, 10, (0, 10))
		self.cells = self.createEntry(self.widget_frame, "Cells range", 0, 1, 10, (0, 10))
		self.min = self.createEntry(self.widget_frame, "Min points", 1, 0, 10, (0, 10))
		self.max = self.createEntry(self.widget_frame, "Max points", 1, 1, 10, (0, 10))
	
		self.widget_frame_graph = ttk.LabelFrame(self.left_frame, text = "Chart Options", style = "Standard.Label")
		self.widget_frame_graph.grid(row = 1, column = 0, padx = 10, pady = (0, 10))

		# Entry fields
		self.chart_type = self.createEntry(self.widget_frame_graph, "Chart Type", 0, 0, 10, (0, 10))
		self.marker = self.createEntry(self.widget_frame_graph, "Point marker", 0, 1, 10, (0, 10))
		self.column_names = self.createEntry(self.widget_frame_graph, "Columns names", 1, 0, 10, (0, 10), 2, sticky = "nsew")

		

		self.widget_frame_settings = ttk.LabelFrame(self.left_frame, text = "Chart Options", style = "Standard.Label")
		self.widget_frame_settings.grid(row = 2, column = 0, padx = 10, pady = (0, 10))

		self.button = ttk.Button(self.widget_frame_settings, text = "Accept", command = self.accepted)
		self.button.grid(row = 0, column = 0, sticky = "nsew", padx = 10)

		self.button_chart = ttk.Button(self.widget_frame_settings, text = "Create Chart", command = self.createChart)
		self.button_chart.grid(row = 0, column = 1, sticky = "nsew")

		# ------------ Data window --------------
		self.right_frame = Frame(self.main_frame)
		self.right_frame.grid(row = 0, column = 1)

		
		self.dataScroll = ttk.Scrollbar(self.right_frame)
		self.dataScroll.pack(side = "right", fill = "y")

		self.cols = ["Columns names"]
		self.dataWindow = ttk.Treeview(self.right_frame, show = "headings", yscrollcommand = self.dataScroll.set, columns = self.cols, height = 13)
		self.dataWindow.pack()
		self.dataScroll.config(command=self.dataWindow.yview)




		self.screen.mainloop()

	def createEntry(self, root, defaultInsert, row, column, padx, pady, columnspan = 1, rowspan = 1,sticky = ""):
		new_entry = ttk.Entry(root)
		new_entry.insert(0, defaultInsert)
		new_entry.bind("<FocusIn>", lambda e: new_entry.delete("0", "end"))
		new_entry.grid(row = row, column = column, padx = padx, pady = pady, columnspan = columnspan, rowspan = rowspan, sticky = sticky)
		return new_entry

	def accepted(self):
		# Basic 
		self.file = self.file_name.get() # Getting a file name
		self.cells_range = self.cells.get()

		# Chart
		self.type = self.chart_type.get()
		self.point_marker = self.marker.get()

		self.cols = self.column_names.get().split(", ")
		self.dataWindow.config(columns = self.cols)

		self.load_data()

	def load_data(self):
		excel = an.openExcel(self.file)
		self.data = an.lookForColms(excel, self.cols)
		#print(self.data)

		#Lodaing data to data window

		for col in self.cols:
			self.dataWindow.heading(col, text = col)

		for index, row in self.data.iterrows():
			new_list = row.values.tolist()
			self.dataWindow.insert("", END , values = new_list)

	def createChart(self):
		an.scatterData(self.data["Serial Nr."], self.data["Value"], "Data Graph", "o")
		an.showPlot()