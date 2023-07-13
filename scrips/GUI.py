from tkinter import *
import tkinter.ttk as ttk
import analize as an

class App(Tk):
	def __init__(self):
		self.screen = Tk()

		# ------------------- Style --------------------------
		style = ttk.Style()
		style.theme_use("alt")
		style.configure(".", foreground = "white", background = "#445663", borderwidth = 1)
		style.configure("TButton", background = "#445663")
		style.map("TButton", foreground = [("pressed", "black"), ("active", "black")])
		style.configure("TLabelframe", bordercolor = "blue", borderwidth = 1)
		style.configure("TEntry", foreground = "black")
		style.configure("TCombobox", foreground = "black")
		style.configure("Treeview", foreground = "black")


		# ---------------- Basic config ----------------------
		self.screen.title("Analizer")
		self.screen.config(bg="black")

		# Menu for More 
		self.main_frame = Frame(self.screen, bg = "#445663")
		self.main_frame.pack()

		# Menu for excel configue nad chart
		self.left_frame = Frame(self.main_frame, bg = "#445663")
		self.left_frame.grid(row = 0, column = 0)

		# ---------- Excel Options ----------
		self.widget_frame = ttk.Labelframe(self.left_frame, text = "Excel Options")
		self.widget_frame.grid(row = 0, column = 0, padx = 10, pady = (0, 10))

		# Entry fields
		self.file_name = self.createEntry(self.widget_frame, "Excel Name", 0, 0, 10, (5, 10))
		self.cells = self.createEntry(self.widget_frame, "Cells range", 0, 1, 10, (5, 10))
		self.min = self.createEntry(self.widget_frame, "Min points", 1, 0, 10, (0, 10))
		self.max = self.createEntry(self.widget_frame, "Max points", 1, 1, 10, (0, 10))

		self.column_names = self.createEntry(self.widget_frame, "Columns names", 2, 0, 10, (0, 10), 2, sticky = "nsew")

		self.button = ttk.Button(self.widget_frame, text = "Accept", command = self.accepted_excel)
		self.button.grid(row = 3, column = 0, sticky = "nsew", padx = 10, pady = (0, 10), columnspan = 2)
		
		# --------- Chart Options ------------
		self.widget_frame_graph = ttk.Labelframe(self.left_frame, text = "Chart Options")
		self.widget_frame_graph.grid(row = 1, column = 0, padx = 10, pady = (5, 10))

		chart_type_text = ttk.Label(self.widget_frame_graph, text = "Chart Type: ", background = "#445663")
		chart_type_text.grid(row = 0, column = 0, padx = 10, pady = (5, 10))
		self.chart_type = self.createCombolist(self.widget_frame_graph, ["Plot", "Scatter"], 0, 1, 10, (5, 10))

		chart_marker_text = ttk.Label(self.widget_frame_graph, text = "Marker: ", background = "#445663")
		chart_marker_text.grid(row = 1, column = 0, padx = 10, pady = (0, 10))
		self.marker = self.createCombolist(self.widget_frame_graph, ["*", "o"], 1, 1, 10, (0, 10))

	
		self.xValues_entry = self.createCombolist(self.widget_frame_graph, ["x values"], 2, 0, 10, (0, 10), columnspan = 2, sticky = "nsew")
		self.yValues_entry = self.createCombolist(self.widget_frame_graph, ["y values"],3, 0, 10, (0, 10), columnspan = 2, sticky = "nsew")

		self.button_chr_option = ttk.Button(self.widget_frame_graph, text = "Accept", state = DISABLED, command = self.accepted_chart)
		self.button_chr_option.grid(row = 4, column = 0, sticky = "nsew", padx = 10, pady = (0, 5), columnspan = 2)

		# Buttons
		self.widget_frame_settings = ttk.Labelframe(self.left_frame, borderwidth = 0)
		self.widget_frame_settings.grid(row = 2, column = 0, padx = 10, pady = (0, 10))

		self.button_chart = ttk.Button(self.widget_frame_settings, text = "Create Chart", command = self.createChart)
		self.button_chart.grid(row = 0, column = 0, sticky = "nsew")

		# ------------ Data window --------------
		self.right_frame = Frame(self.main_frame, bg = "#445663")
		self.right_frame.grid(row = 0, column = 1)

		
		self.dataScroll = ttk.Scrollbar(self.right_frame)
		self.dataScroll.pack(side = "right", fill = "y")

		self.cols = ["Columns names"]
		self.dataWindow = ttk.Treeview(self.right_frame, show = "headings", yscrollcommand = self.dataScroll.set, columns = self.cols, height = 20)
		self.dataWindow.pack()
		self.dataScroll.config(command=self.dataWindow.yview)

		self.screen.mainloop()

	def createEntry(self, root, defaultInsert, row, column, padx, pady, columnspan = 1, rowspan = 1,sticky = ""):
		new_entry = ttk.Entry(root, background = "#445663")
		new_entry.insert(0, defaultInsert)
		new_entry.bind("<FocusIn>", lambda e: new_entry.delete("0", "end"))
		new_entry.grid(row = row, column = column, padx = padx, pady = pady, columnspan = columnspan, rowspan = rowspan, sticky = sticky)
		return new_entry

	def createCombolist(self, root, combo_list, row, column, padx, pady, columnspan = 1, rowspan = 1,sticky = ""):
		new_combo = ttk.Combobox(root, values = combo_list)
		new_combo.current(0)
		new_combo.grid(row = row, column = column, padx = padx, pady = pady, columnspan = columnspan, rowspan = rowspan, sticky = sticky)
		return new_combo

	def accepted_excel(self):
		# Basic 
		self.file = self.file_name.get() # Getting a file name
		self.cells_range = self.cells.get()

		self.min_val = self.min.get() 
		self.max_val = self.max.get()

		self.cols = self.column_names.get().split(", ")
		self.dataWindow.config(columns = self.cols)

		self.xValues_entry.config(values = self.cols)
		self.xValues_entry.current(0)
		self.yValues_entry.config(values = self.cols)
		self.yValues_entry.current(0)

		self.button_chr_option.config(state = NORMAL)

		self.load_data()

	def accepted_chart(self):
		self.type = self.chart_type.get()
		self.point_marker = self.marker.get()

		self.xValues = self.xValues_entry.get().split(", ")
		self.yValues = self.yValues_entry.get().split(", ")

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
		if self.type == "Scatter":
			an.scatterData(self.data["Serial Nr."], self.data["Value"], "Data Graph", "o")
			an.showPlot()