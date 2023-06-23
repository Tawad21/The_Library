class BooksController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.frames['books'].table.insert_rows(
            self.model.database.execute_query('SELECT title, author, genre, language, book_id FROM books'))
        self._bind()

    def _bind(self):
        # Add keyboard/button controls for entries
        self.view.frames['books'].search_bar.entry.bind(
            '<Return>', lambda e: self.find(self.view.frames['books'].search_bar.get_search_input()))
        self.view.frames['books'].search_bar.button.configure(
            command=lambda: self.find(self.view.frames['books'].search_bar.get_search_input()))
        
        self.view.frames['books'].add_button.configure(command=self.show_add_form)
        self.view.frames['books'].edit_button.configure(command=self.show_edit_form)
        self.view.frames['books'].data_form.cancel_button.configure(command=self.cancel_form)

    def cancel_form(self):
        self.view.frames['books'].hide_form()
        self.view.frames['books'].show_widgets()

    def show_add_form(self):
        self.view.frames['books'].hide_widgets()
        self.view.frames['books'].show_form('Add book')
        self.view.frames['books'].data_form.confirm_button.configure(command=self.add_book)
    
    def show_edit_form(self):
        #get selection
        book = self.view.frames['books'].table.get_selection()

        #check selection
        if book == 'no selection':
            self.view.give_error_message('please select a book to edit')
            return

        #switch widgets
        self.view.frames['books'].hide_widgets()
        self.view.frames['books'].show_form('Edit book')
        self.view.frames['books'].data_form.fill_entries(book['values'][0:4])
        self.view.frames['books'].data_form.confirm_button.configure(command=self.edit_book)

    def add_book(self):
        #gets imputted data from the user 
        book_data = self.view.frames['books'].data_form.get_data_from_entries()

        #adds book to database
        self.model.book_model.add_book(book_data)

        #update the table and return to it
        self.find(self.view.frames['books'].search_bar.get_search_input())
        self.cancel_form()
    
    def edit_book(self):
        #gets imputted data from the user and the id from the book that is to be edited
        book_data = self.view.frames['books'].data_form.get_data_from_entries()
        book_id =  self.view.frames['books'].table.get_selection()['values'][4]

        #edits book in the database
        self.model.book_model.edit_book(book_data, book_id)

        #update tables and return close form
        self.find(self.view.frames['books'].search_bar.get_search_input())
        self.find(self.view.frames['lent'].search_bar.get_search_input())
        self.cancel_form()

    def find(self, search_input):
        self.view.frames['books'].table.clear_rows()
        search_column = self.view.frames['books'].search_bar.get_selected_column()
        self.view.frames['books'].table.insert_rows(self.model.book_model.search_books(search_column, search_input))
    

        
 