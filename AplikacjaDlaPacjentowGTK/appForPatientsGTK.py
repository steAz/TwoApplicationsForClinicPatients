import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio
from medicalModule import Medical_information
import copy

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='BasicMenu'>
      <menuitem action='BasicAbout' />
      <menuitem action='BasicQuit' />
    </menu>
    <menu action='VisitsMenu'>
      <menu action='VisitsPreviewMenu'>
        <menuitem action='VisitsUpcoming' />
        <menuitem action='VisitsFinished' />
      </menu>
      <menuitem action='VisitsNew' />
    </menu>
    <menu action='ClinicsMenu'>
      <menuitem action='ClinicJaskolska' />
      <menuitem action='ClinicTowarowa' />
      <menuitem action='ClinicJanowicza' />
    </menu>
  </menubar>
</ui>
"""

class MenuExampleWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Aplikacja przeznaczona dla pacjenta przychodni Medyk")

        self.set_default_size(1020, 500)
        self.set_resizable(False)

        self.medical_information = Medical_information()
        self.actual_new_visit = None

        action_group = Gtk.ActionGroup("my_actions")

        self.add_basic_menu_actions(action_group)
        self.add_visits_menu_actions(action_group)
        self.add_clinics_menu_actions(action_group)

        uimanager = self.create_ui_manager()
        uimanager.insert_action_group(action_group)

        menubar = uimanager.get_widget("/MenuBar")

        self.grid = Gtk.Grid()
        self.grid.add(menubar)
        self.add(self.grid)

    def add_basic_menu_actions(self, action_group):
        action_basic_menu = Gtk.Action("BasicMenu", "Program", None, None)
        action_group.add_action(action_basic_menu)

        action_basic_about = Gtk.Action("BasicAbout", "O programie", None, None)
        action_basic_about.connect("activate", self.on_menu_basic_about)
        action_group.add_action(action_basic_about)

        action_basic_quit = Gtk.Action("BasicQuit", None, None, Gtk.STOCK_QUIT)
        action_basic_quit.connect("activate", self.on_menu_basic_quit)
        action_group.add_action_with_accel(action_basic_quit, '<Control>Q')


    def add_visits_menu_actions(self, action_group):
        action_visits_menu = Gtk.Action("VisitsMenu", "Wizyty", None, None)
        action_group.add_action(action_visits_menu)
        
        action_group.add_action(Gtk.Action("VisitsPreviewMenu", "Podgląd wizyt", None,
            None))
        
        action_visit_new = Gtk.Action("VisitsNew", "Umów wizytę", None, None)
        action_visit_new.connect("activate", self.on_menu_visit_new)
        action_group.add_action_with_accel(action_visit_new, '<Control>N')

        action_visits_upcoming = Gtk.Action("VisitsUpcoming", "Nadchodzące wizyty", None, None)
        action_visits_upcoming.connect("activate", self.on_menu_visits_upcoming)
        action_group.add_action(action_visits_upcoming)

        action_visits_finished = Gtk.Action("VisitsFinished", "Zakończone wizyty", None, None)
        action_visits_finished.connect("activate", self.on_menu_visits_finished)
        action_group.add_action(action_visits_finished)


    def add_clinics_menu_actions(self, action_group):
        action_clinics_menu = Gtk.Action("ClinicsMenu", "Kontakt", None, None)
        action_group.add_action(action_clinics_menu)

        action_clinic_jaskolska = Gtk.Action("ClinicJaskolska", "Przychodnia Jaskólska", None, None)
        action_clinic_jaskolska.connect("activate", self.on_menu_clinic_jaskolska)
        action_group.add_action(action_clinic_jaskolska)

        action_clinic_towarowa = Gtk.Action("ClinicTowarowa", "Przychodnia Towarowa", None, None)
        action_clinic_towarowa.connect("activate", self.on_menu_clinic_towarowa)
        action_group.add_action(action_clinic_towarowa)

        action_clinic_janowicza = Gtk.Action("ClinicJanowicza", "Przychodnia Janowicza", None, None)
        action_clinic_janowicza.connect("activate", self.on_menu_clinic_janowicza)
        action_group.add_action(action_clinic_janowicza)


    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager


    def on_menu_visit_new(self, widget):
        print("Pressed 'new visit' menuitem")
        self.clear_elements_without_menu(True)
        label = Gtk.Label("Wybierz wolny termin i akceptuj przyciskiem na dole")
        self.grid.attach(label, 0, 1, 1, 1) # LEFT, TOP, WIDTH, HEIGHT
        label.show()
        self.display_tree_list_with_visits(self.medical_information.new_visits)
        button = Gtk.Button("Umów wizytę")
        button.connect("clicked", self.on_selection_new_visit_button_clicked)
        self.grid.attach(button, 0, 4, 1, 1)
        button.show()
        tree_selection = self.treeview.get_selection()
        #tree_selection.set_mode(Gtk.SELECTION_MULTIPLE)
        tree_selection.connect("changed", self.on_tree_selection_changed_while_new_visit)

        

    def doctor_filter_func(self, model, iter, data):
        """Tests if the doctor in the row is the one in the filter"""
        if self.current_filter_doctor is None or self.current_filter_doctor == "Bez filtrowania":
            return True
        else:
            return model[iter][0] == self.current_filter_doctor
    # Delete elements that are not needed in the window
    def clear_elements_without_menu(self, clear_actual_new_visit):
        #self.grid.remove_row(2)
        for x in range(0, 10):
            self.grid.remove_row(1)

        if clear_actual_new_visit == True:
            self.actual_new_visit = None

    def on_menu_visits_upcoming(self, widget):
        print("Pressed 'upcoming visits' menuitem")
        self.clear_elements_without_menu(True)
        self.display_tree_list_with_visits(self.medical_information.upcoming_visits)
    
    def on_menu_visits_finished(self, widget):
        print("Pressed 'finished visits' menuitem")
        self.clear_elements_without_menu(True)
        self.display_tree_list_with_visits(self.medical_information.finished_visits) 

    def on_menu_basic_about(self, widget):
        self.clear_elements_without_menu(True)
        label = Gtk.Label("Aplikacja jest przeznaczona dla pacjentów przychodni Medyk znajdujących się w mieście Sopot.\n"
                            "Program pozwala na:\n"
                            "   - umówienie się na wizytę do konkretnego lekarza POZ wraz z miejscem, datą i godziną wizyty\n"
                            "   - podgląd wizyt (nadchodzących oraz tych, które się odbyły) wraz ze szczegółami\n"
                            "   - sprawdzenie kontaktu z placówkami przychodni Medyk\n"
                            "Autor: Michał Kazanowski\n")
        
        self.grid.attach(label, 0, 1, 20, 1) # LEFT, TOP, WIDTH, HEIGHT
        label.show()


    def on_menu_basic_quit(self, widget):
        Gtk.main_quit()
        #self.grid.remove_row(2)

    def on_menu_clinic_jaskolska(self, widget):
        self.clear_elements_without_menu(True)
        label = Gtk.Label("Przychodnia Medyk\n"
                            "   ul. Jaskólska 2\n"
                            "   80-743, Sopot\n"
                            "   Telefoniczna rejestracja oraz informacja: 224192997\n")
        
        self.grid.attach(label, 0, 1, 20, 1) # LEFT, TOP, WIDTH, HEIGHT
        label.show()


    def on_menu_clinic_towarowa(self, widget):
        self.clear_elements_without_menu(True)
        label = Gtk.Label("Przychodnia Medyk\n"
                            "   ul. Towarowa 15\n"
                            "   80-330 Sopot\n"
                            "   Telefoniczna rejestracja oraz informacja: 224192998\n")
        
        self.grid.attach(label, 0, 1, 20, 1) # LEFT, TOP, WIDTH, HEIGHT
        label.show()


    def on_menu_clinic_janowicza(self, widget):
        self.clear_elements_without_menu(True)
        label = Gtk.Label("Przychodnia Medyk\n"
                            "   ul. Janowicza 5\n"
                            "   80-001 Sopot\n"
                            "   Telefoniczna rejestracja oraz informacja: 224192999\n")
        
        self.grid.attach(label, 0, 1, 20, 1) # LEFT, TOP, WIDTH, HEIGHT
        label.show()

    def on_selection_filtering_button_clicked(self, widget):
        #we set the current doctor filter to the button's label
        self.current_filter_doctor = widget.get_label()
        print("%s doctor selected!" % self.current_filter_doctor)
        #we update the filter, which updates in turn the view
        self.doctor_filter.refilter()

    def on_selection_new_visit_button_clicked(self, widget):
        print("Pressed 'add new visit' button")

        self.clear_elements_without_menu(False)
        
        self.display_tree_list_with_visits(self.medical_information.new_visits)
        button = Gtk.Button("Umów wizytę")
        button.connect("clicked", self.on_selection_new_visit_button_clicked)
        self.grid.attach(button, 0, 4, 1, 1)
        button.show()
        tree_selection = self.treeview.get_selection()
        #tree_selection.set_mode(Gtk.SELECTION_MULTIPLE)
        tree_selection.connect("changed", self.on_tree_selection_changed_while_new_visit)

        if self.actual_new_visit is None:
            print("none actual")
            label = Gtk.Label("Wybierz wolny termin i akceptuj przyciskiem na dole.\n"
                               "Nie udało się zaplanować wizyty, wybierz termin z listy.")
            self.grid.attach(label, 0, 1, 1, 1) # LEFT, TOP, WIDTH, HEIGHT
            label.show()
        else:
            print("there is actual")
            actualNewVisit = copy.deepcopy(self.actual_new_visit)
            self.medical_information.upcoming_visits.append(actualNewVisit)
            self.medical_information.new_visits.remove(actualNewVisit)
            label = Gtk.Label("Wybierz wolny termin i akceptuj przyciskiem na dole.\n"
                               "Umówiono wizytę.")
            self.grid.attach(label, 0, 1, 1, 1) # LEFT, TOP, WIDTH, HEIGHT
            label.show()
            self.actual_new_visit = None

    def on_tree_selection_changed_while_new_visit(self, tree_selection):
        (model, pathlist) = tree_selection.get_selected_rows()
        for path in pathlist :
            tree_iter = model.get_iter(path)
            self.actual_new_visit = copy.deepcopy((model.get_value(tree_iter , 0,), # elements of each column give whole visit
                                     model.get_value(tree_iter , 1,),
                                     model.get_value(tree_iter , 2,),
                                     model.get_value(tree_iter , 3,)))
            print("Actual new visit: ", self.actual_new_visit)


    def display_tree_list_with_visits(self, visits_list):
        #Creating the ListStore model
        self.new_visit_liststore = Gtk.ListStore(str, str, str, str)
        for visit_ref in visits_list:
            self.new_visit_liststore.append(list(visit_ref))
        self.current_filter_doctor = None

        #Creating the filter, feeding it with the liststore model
        self.doctor_filter = self.new_visit_liststore.filter_new()
        #setting the filter function, note that we're not using the
        self.doctor_filter.set_visible_func(self.doctor_filter_func)

        #creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.doctor_filter)
        for i, column_title in enumerate(["Imię i nazwisko lekarza", "Przychodnia", "Dzień", "Godzina"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        #creating buttons to filter by programming doctor, and setting up their events
        self.buttons = list()
        for prog_doctor in ["Adam Stanowski", "Małgorzata Kowalska", "Edmund Nowak", "Piotr Rojek", "Alicja Konstantynowicz", "Bez filtrowania"]:
            button = Gtk.Button(prog_doctor)
            self.buttons.append(button)
            button.connect("clicked", self.on_selection_filtering_button_clicked)

        #setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 2, 20, 1)
        self.scrollable_treelist.add(self.treeview)

        label = Gtk.Label("Filtruj:")
        self.grid.attach_next_to(label, self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.buttons[0], label, Gtk.PositionType.RIGHT, 1, 1)
        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)

        self.show_all()

window = MenuExampleWindow()        
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()