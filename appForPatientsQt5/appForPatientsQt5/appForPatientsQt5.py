import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt5.QtWidgets import QAbstractItemView, QPushButton, QSizePolicy
from PyQt5.QtGui import QIcon
from medicalModule import Medical_information
import copy

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Aplikacja przeznaczona dla pacjenta przychodni Medyk'
        self.left = 10
        self.top = 60
        self.width = 768
        self.height = 576
        self.medical_info = Medical_information()
        self.aboutLabel = None
        self.finishedVisitsTableWidget = None
        self.filterLabel = None
        self.firstDoctorNameButton = None
        self.secDoctorNameButton = None
        self.thirdDoctorNameButton = None
        self.fourthDoctorNameButton = None
        self.fifthDoctorNameButton = None
        self.withoutFilteringButton = None
        self.makeAppointmentButton = None
        self.makeAppointmentLabel = None
        self.actualNewVisit = None
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        mainMenu = self.menuBar()
        basicMenu = mainMenu.addMenu('Program')

        basicAboutAction = QAction("O programie", self)
        basicAboutAction.setStatusTip('Pokaż szczegółowy opis aplikacji')
        basicAboutAction.triggered.connect(self.show_info_about_app)
        basicMenu.addAction(basicAboutAction)

        basicQuitButton = QAction('Zakończ', self)
        basicQuitButton.setShortcut('Ctrl+Q')
        basicQuitButton.setStatusTip('Wyłącz aplikację')
        basicQuitButton.triggered.connect(self.close)
        basicMenu.addAction(basicQuitButton)


        visitsMenu = mainMenu.addMenu('Wizyty')
        visitsPreviewOfVisitsMenu = visitsMenu.addMenu('Podgląd wizyt')

        visitsUpcomingVisitsAction = QAction("Nadchodzące wizyty", self)
        visitsUpcomingVisitsAction.setStatusTip('Zobacz nadchodzące wizyty')
        visitsUpcomingVisitsAction.triggered.connect(self.show_upcoming_visits)
        visitsPreviewOfVisitsMenu.addAction(visitsUpcomingVisitsAction)

        visitsFinishedVisitsAction = QAction("Zakończone wizyty", self)
        visitsFinishedVisitsAction.setStatusTip('Zobacz zakończone wizyty')
        visitsFinishedVisitsAction.triggered.connect(self.show_finished_visits)
        visitsPreviewOfVisitsMenu.addAction(visitsFinishedVisitsAction)

        visitsMakeAppointmentAction = QAction("Umów wizytę", self)
        visitsMakeAppointmentAction.setShortcut('Ctrl+N')
        visitsMakeAppointmentAction.setStatusTip('Umów wizytę wybierając odpowiednie opcje')
        visitsMakeAppointmentAction.triggered.connect(self.make_appointment)
        visitsMenu.addAction(visitsMakeAppointmentAction)

        contactMenu = mainMenu.addMenu('Kontakt')

        clinicJaskolskaAction = QAction("Przychodnia Jaskólska", self)
        clinicJaskolskaAction.setStatusTip('Pokaż dane przychodni na Jaskólskiej')
        clinicJaskolskaAction.triggered.connect(self.show_clinic_jaskolska_info)
        contactMenu.addAction(clinicJaskolskaAction)

        clinicTowarowaAction = QAction("Przychodnia Towarowa", self)
        clinicTowarowaAction.setStatusTip('Pokaż dane przychodni na Towarowej')
        clinicTowarowaAction.triggered.connect(self.show_clinic_towarowa_info)
        contactMenu.addAction(clinicTowarowaAction)

        clinicJanowiczaAction = QAction("Przychodnia Janowicza", self)
        clinicJanowiczaAction.setStatusTip('Pokaż dane przychodni na Janowicza')
        clinicJanowiczaAction.triggered.connect(self.show_clinic_janowicza_info)
        contactMenu.addAction(clinicJanowiczaAction)

        self.myLayout = QHBoxLayout()
        main = QWidget(self)
        main.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(main)
        self.centralWidget().setLayout(self.myLayout)
        self.show()

    def show_info_about_app(self):
        self.clearElementsFromMainWindow()

        self.aboutLabel = QLabel(self)
        self.aboutLabel.setText("Aplikacja jest przeznaczona dla pacjentów przychodni Medyk znajdujących się w mieście Sopot.\n"
                            "Program pozwala na:\n"
                            "   - umówienie się na wizytę do konkretnego lekarza POZ wraz z miejscem, datą i godziną wizyty\n"
                            "   - podgląd wizyt (nadchodzących oraz tych, które się odbyły) wraz ze szczegółami\n"
                            "   - sprawdzenie kontaktu z placówkami przychodni Medyk\n"
                            "Autor: Michał Kazanowski\n")
        self.aboutLabel.move(3, 30)
        self.aboutLabel.setFixedWidth(500)
        self.aboutLabel.setFixedHeight(85)
        self.aboutLabel.show()

    def show_clinic_jaskolska_info(self):
        self.clearElementsFromMainWindow()

        self.aboutLabel = QLabel(self)
        self.aboutLabel.setText("Przychodnia Medyk\n"
                            "   ul. Jaskólska 2\n"
                            "   80-743, Sopot\n"
                            "   Telefoniczna rejestracja oraz informacja: 224192997\n")
        self.aboutLabel.move(3, 30)
        self.aboutLabel.setFixedWidth(300)
        self.aboutLabel.setFixedHeight(50)
        self.aboutLabel.show()

    def show_clinic_towarowa_info(self):
        self.clearElementsFromMainWindow()

        self.aboutLabel = QLabel(self)
        self.aboutLabel.setText("Przychodnia Medyk\n"
                            "   ul. Towarowa 15\n"
                            "   80-330 Sopot\n"
                            "   Telefoniczna rejestracja oraz informacja: 224192998\n")
        self.aboutLabel.move(3, 30)
        self.aboutLabel.setFixedWidth(300)
        self.aboutLabel.setFixedHeight(50)
        self.aboutLabel.show()

    def show_clinic_janowicza_info(self):
        self.clearElementsFromMainWindow()

        self.aboutLabel = QLabel(self)
        self.aboutLabel.setText("Przychodnia Medyk\n"
                            "   ul. Janowicza 5\n"
                            "   80-001 Sopot\n"
                            "   Telefoniczna rejestracja oraz informacja: 224192999\n")
        self.aboutLabel.move(3, 30)
        self.aboutLabel.setFixedWidth(300)
        self.aboutLabel.setFixedHeight(50)
        self.aboutLabel.show()

    def make_appointment(self):
        self.clearElementsFromMainWindow()
        self.createGuiForVisitsTable(self.medical_info.new_visits)

        self.makeAppointmentLabel = QLabel(self)
        self.makeAppointmentLabel.setText("Wybierz wolny termin i akceptuj przyciskiem na dole")
        self.makeAppointmentLabel.move(450,60)
        self.makeAppointmentLabel.setFixedWidth(400)
        self.makeAppointmentLabel.show()

        heightOfTable = (len(self.medical_info.new_visits) + 1)*29.5
        self.makeAppointmentButton = QPushButton("Umów wizytę", self)
        self.makeAppointmentButton.setObjectName("Umów wizytę")
        self.makeAppointmentButton.setStatusTip('Umawia wizytę')
        self.makeAppointmentButton.clicked.connect(self.onSelectionNewVisitButtonClicked)
        self.makeAppointmentButton.move(30, 30 + heightOfTable + 35)
        self.makeAppointmentButton.show()



    def clearElementsFromMainWindow(self):
        if self.aboutLabel != None: self.aboutLabel.hide()
        if self.finishedVisitsTableWidget != None:
            for i in reversed(range(self.centralWidget().layout().count())):
                self.centralWidget().layout().itemAt(i).widget().setParent(None)
        if self.filterLabel != None: self.filterLabel.hide()
        if self.firstDoctorNameButton != None: self.firstDoctorNameButton.hide()
        if self.secDoctorNameButton != None: self.secDoctorNameButton.hide()
        if self.thirdDoctorNameButton != None: self.thirdDoctorNameButton.hide()
        if self.fourthDoctorNameButton != None: self.fourthDoctorNameButton.hide()
        if self.fifthDoctorNameButton != None: self.fifthDoctorNameButton.hide()
        if self.withoutFilteringButton != None: self.withoutFilteringButton.hide()
        if self.makeAppointmentButton != None: self.makeAppointmentButton.hide()
        if self.makeAppointmentLabel != None: self.makeAppointmentLabel.hide()

    def show_upcoming_visits(self):
        self.clearElementsFromMainWindow()
        self.createGuiForVisitsTable(self.medical_info.upcoming_visits)

    def createGuiForVisitsTable(self, visits):
        self.finishedVisitsTableWidget = QTableWidget(self)
        self.finishedVisitsTableWidget.setColumnCount(4)
        self.finishedVisitsTableWidget.setRowCount(len(visits))
        self.finishedVisitsTableWidget.setHorizontalHeaderLabels(['Imię i nazwisko lekarza', 'Adres przychodni', 'Dzień', 'Godzina'])
        self.finishedVisitsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.finishedVisitsTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        #self.finishedVisitsTableWidget.move(10,25)

        heightOfTable = (len(visits) + 1)*29.5
        self.finishedVisitsTableWidget.setGeometry(3, 30, 386.5, heightOfTable)
        self.finishedVisitsTableWidget.setColumnWidth(0, 150)
        self.finishedVisitsTableWidget.setColumnWidth(1, 110)
        self.finishedVisitsTableWidget.setColumnWidth(2, 47)
        self.finishedVisitsTableWidget.setColumnWidth(3, 60)
        counter = 0
        for oneTuple in visits:
            self.finishedVisitsTableWidget.setItem(counter, 0, QTableWidgetItem(oneTuple[0]))
            self.finishedVisitsTableWidget.setItem(counter, 1, QTableWidgetItem(oneTuple[1]))
            self.finishedVisitsTableWidget.setItem(counter, 2, QTableWidgetItem(oneTuple[2]))
            self.finishedVisitsTableWidget.setItem(counter, 3, QTableWidgetItem(oneTuple[3]))
            counter += 1

        self.centralWidget().layout().addWidget(self.finishedVisitsTableWidget)

        self.filterLabel = QLabel(self)
        self.filterLabel.setText("Filtruj:")
        self.filterLabel.move(30, 30 + heightOfTable + 5)
        self.filterLabel.show()

        self.firstDoctorNameButton = QPushButton("Adam Stanowski", self)
        self.firstDoctorNameButton.setObjectName("Adam Stanowski")
        self.firstDoctorNameButton.setStatusTip('Filtruj po Adamie Stanowskim')
        self.firstDoctorNameButton.clicked.connect(self.filter_by_doctor_name)
        self.firstDoctorNameButton.move(60, 30 + heightOfTable + 5)
        self.firstDoctorNameButton.show()

        self.secDoctorNameButton = QPushButton("Małgorzata Kowalska", self)
        self.secDoctorNameButton.setObjectName("Małgorzata Kowalska")
        self.secDoctorNameButton.setStatusTip('Filtruj po Małgorzacie Kowalskiej')
        self.secDoctorNameButton.clicked.connect(self.filter_by_doctor_name)
        self.secDoctorNameButton.move(160, 30 + heightOfTable + 5)
        self.secDoctorNameButton.setFixedWidth(120)
        self.secDoctorNameButton.show()

        self.thirdDoctorNameButton = QPushButton("Edmund Nowak", self)
        self.thirdDoctorNameButton.setObjectName("Edmund Nowak")
        self.thirdDoctorNameButton.setStatusTip('Filtruj po Edmundzie Nowaku')
        self.thirdDoctorNameButton.clicked.connect(self.filter_by_doctor_name)
        self.thirdDoctorNameButton.move(280, 30 + heightOfTable + 5)
        self.thirdDoctorNameButton.show()

        self.fourthDoctorNameButton = QPushButton("Piotr Rojek", self)
        self.fourthDoctorNameButton.setObjectName("Piotr Rojek")
        self.fourthDoctorNameButton.setStatusTip('Filtruj po Piotrze Rojku')
        self.fourthDoctorNameButton.clicked.connect(self.filter_by_doctor_name)
        self.fourthDoctorNameButton.move(380, 30 + heightOfTable + 5)
        self.fourthDoctorNameButton.show()

        self.fifthDoctorNameButton = QPushButton("Alicja Konstantynowicz", self)
        self.fifthDoctorNameButton.setObjectName("Alicja Konstantynowicz")
        self.fifthDoctorNameButton.setStatusTip('Filtruj po Alicji Konstantynowicz')
        self.fifthDoctorNameButton.clicked.connect(self.filter_by_doctor_name)
        self.fifthDoctorNameButton.move(480, 30 + heightOfTable + 5)
        self.fifthDoctorNameButton.setFixedWidth(130)
        self.fifthDoctorNameButton.show()

        self.withoutFilteringButton = QPushButton("Bez filtrowania", self)
        self.withoutFilteringButton.setObjectName("Bez filtrowania")
        self.withoutFilteringButton.setStatusTip('Nie filtruj')
        self.withoutFilteringButton.clicked.connect(self.filter_by_doctor_name)
        self.withoutFilteringButton.move(610, 30 + heightOfTable + 5)
        self.withoutFilteringButton.show()

    def show_finished_visits(self):
        self.clearElementsFromMainWindow()
        self.createGuiForVisitsTable(self.medical_info.finished_visits)

    def filter_by_doctor_name(self):
        for i in range(self.finishedVisitsTableWidget.rowCount()):
            self.finishedVisitsTableWidget.setRowHidden(i, False)

        sending_button = self.sender()
        filterString = str(sending_button.objectName())

        if filterString != "Bez filtrowania":
            for i in range(self.finishedVisitsTableWidget.rowCount()):
                match = False
                item  = self.finishedVisitsTableWidget.item(i, 0)
                if item.text() == filterString:
                    match = True
                self.finishedVisitsTableWidget.setRowHidden(i, not match)

    def onSelectionNewVisitButtonClicked(self):
        currentItem = self.finishedVisitsTableWidget.currentItem()
        currentRow = self.finishedVisitsTableWidget.currentRow()
        if(currentItem is None):
            print("none currentItem")
            self.makeAppointmentLabel.setText("Wybierz wolny termin i akceptuj przyciskiem na dole.\n"
                                                "Nie udało się zaplanować wizyty, wybierz termin z listy.")
        else:
            print("there is currentItem")
            self.makeAppointmentLabel.setText("Wybierz wolny termin i akceptuj przyciskiem na dole.\n"
                                                "Umówiono wizytę.")
            nameOfDoctor = self.finishedVisitsTableWidget.item(currentRow, 0)
            district = self.finishedVisitsTableWidget.item(currentRow, 1)
            dateOfVisit = self.finishedVisitsTableWidget.item(currentRow, 2)
            hourOfVisit = self.finishedVisitsTableWidget.item(currentRow, 3)
            self.actualNewVisit = (copy.deepcopy(nameOfDoctor.text()), copy.deepcopy(district.text()),
                                   copy.deepcopy(dateOfVisit.text()), copy.deepcopy(hourOfVisit.text()))
            self.finishedVisitsTableWidget.removeRow(currentRow)
            self.medical_info.new_visits.remove(self.actualNewVisit)
            self.medical_info.upcoming_visits.append(self.actualNewVisit)
            self.finishedVisitsTableWidget.setCurrentItem(None)
            self.withoutFilteringButton.click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
