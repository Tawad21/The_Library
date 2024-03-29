import customtkinter as ctk
from PIL import Image
import os

from src.resources.config import IMAGES_DIR


class SidebarView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.master = master

        # load images
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(IMAGES_DIR, 'customtkinter_logo_single.png')),
                                       size=(30, 30))
        self.overview_image = ctk.CTkImage(light_image=Image.open(os.path.join(IMAGES_DIR, 'overview_dark.png')),
                                           size=(25, 25))
        self.clients_image = ctk.CTkImage(light_image=Image.open(os.path.join(IMAGES_DIR, 'clients_dark.png')),
                                          size=(25, 25))
        self.books_image = ctk.CTkImage(light_image=Image.open(os.path.join(IMAGES_DIR, 'books_dark.png')),
                                        size=(25, 25))
        self.logout_image = ctk.CTkImage(light_image=Image.open(os.path.join(IMAGES_DIR, 'logout_dark.png')),
                                         size=(25, 25))
        self.lent_image = ctk.CTkImage(light_image=Image.open(os.path.join(IMAGES_DIR, 'lent_dark.png')),
                                       size=(25, 25))
        self.calendar_image = ctk.CTkImage(light_image=Image.open(os.path.join(IMAGES_DIR, 'calendar.png')),
                                         size=(25, 25))

        self._create_widgets()

    def _create_widgets(self):
        self.label = ctk.CTkLabel(self, text='  Library Manager',
                                  image=self.logo_image,
                                  compound='left', font=ctk.CTkFont(size=15, weight='bold'))
        self.label.pack(side=ctk.TOP, padx=20, pady=20)

        self.overview_button = ctk.CTkButton(self, corner_radius=0, height=65, border_spacing=10,
                                             text='Overview', fg_color='transparent', text_color=('gray10', 'gray90'),
                                             hover_color=('gray70', 'gray30'), image=self.overview_image, anchor='w', 
                                             font=ctk.CTkFont(size=14))
        self.overview_button.pack(side=ctk.TOP, fill=ctk.X)

        self.books_button = ctk.CTkButton(self, corner_radius=0, height=65, border_spacing=10,
                                          text='Books', fg_color='transparent', text_color=('gray10', 'gray90'),
                                          hover_color=('gray70', 'gray30'), image=self.books_image, anchor='w', state=ctk.NORMAL, 
                                          font=ctk.CTkFont(size=14))
        self.books_button.pack(side=ctk.TOP, fill=ctk.X)

        self.clients_button = ctk.CTkButton(self, corner_radius=0, height=65, border_spacing=10,
                                            text='Clients', fg_color='transparent', text_color=('gray10', 'gray90'),
                                            hover_color=('gray70', 'gray30'), image=self.clients_image, anchor='w', state=ctk.NORMAL, 
                                            font=ctk.CTkFont(size=14))
        self.clients_button.pack(side=ctk.TOP, fill=ctk.X)

        self.lent_button = ctk.CTkButton(self, corner_radius=0, height=65, border_spacing=10,
                                         text='Lent', fg_color='transparent', text_color=('gray10', 'gray90'),
                                         hover_color=('gray70', 'gray30'), image=self.lent_image, anchor='w', 
                                         font=ctk.CTkFont(size=14))
        self.lent_button.pack(side=ctk.TOP, fill=ctk.X)

        self.calendar_button = ctk.CTkButton(self, corner_radius=0, height=65, border_spacing=10,
                                                text='Calendar', fg_color='transparent',
                                                text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'),
                                                image=self.calendar_image, anchor='w')
        self.calendar_button.pack(side=ctk.TOP, fill=ctk.X)

        self.logout_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10,
                                           text='Logout', font=ctk.CTkFont(size=15, weight='bold'),
                                           image=self.logout_image, anchor='w')
        self.logout_button.pack(side=ctk.BOTTOM, fill=ctk.X, pady=(0, 20))

    def toggle_visibility(self, visible: bool):
        if visible:
            self.grid()
            self.books_button.pack_forget()
            self.calendar_button.pack_forget()
            self.lent_button.pack_forget()
            self.clients_button.pack_forget()
            self.overview_button.pack_forget()
            self.overview_button.pack(side=ctk.TOP, fill=ctk.X)
            self.books_button.pack(side=ctk.TOP, fill=ctk.X)
            self.clients_button.pack(side=ctk.TOP, fill=ctk.X)
            self.lent_button.pack(side=ctk.TOP, fill=ctk.X)
            self.calendar_button.pack(side=ctk.TOP, fill=ctk.X)
        else:
            self.grid_remove()

    def toggle_singlevisible(self, visible: bool):
        if visible:
            self.grid()
            self.calendar_button.pack_forget()
            self.lent_button.pack_forget()
            self.clients_button.pack_forget()
            self.overview_button.pack_forget()
            self.grid()
        else:
            self.grid_remove()

    def highlight_sidebar_selection(self, name):
        # show sidebar selected item
        self.overview_button.configure(fg_color=('gray75', 'gray25') if name == 'overview' else 'transparent')
        self.books_button.configure(fg_color=('gray75', 'gray25') if name == 'books' else 'transparent')
        self.clients_button.configure(fg_color=('gray75', 'gray25') if name == 'clients' else 'transparent')
        self.lent_button.configure(fg_color=('gray75', 'gray25') if name == 'lent' else 'transparent')
        self.calendar_button.configure(fg_color=('gray75', 'gray25') if name == 'calendar' else 'transparent')
