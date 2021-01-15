#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Class with some medical information
class Medical_information:
    # Create new visit
    def __init__(self):

        #list of tuples for each visit containing the name of the doctor, the address, the date and the hour of the visit
        self.new_visits = [("Adam Stanowski", "Jaskólska 2", "04-06-19",  "08:00"),
                 ("Adam Stanowski", "Jaskólska 2", "04-06-19", "08:20" ),
                 ("Adam Stanowski", "Towarowa 15", "05-06-19", "12:00"),
                 ("Małgorzata Kowalska", "Towarowa 15", "04-06-19",  "09:00"),
                 ("Małgorzata Kowalska", "Towarowa 15", "04-06-19",  "09:20"),
                 ("Małgorzata Kowalska", "Jaskólska 2", "05-06-19",  "09:00"),
                 ("Edmund Nowak", "Jaskólska 2", "04-06-19",  "08:40"),
                 ("Edmund Nowak", "Jaskólska 2", "04-06-19",  "09:00"),
                 ("Piotr Rojek", "Towarowa 15", "04-06-19",  "09:20"),
                 ("Alicja Konstantynowicz", "Janowicza 5", "04-06-19",  "08:00"),
                 ("Alicja Konstantynowicz", "Janowicza 5", "04-06-19",  "10:00")]

        self.finished_visits = [("Małgorzata Kowalska", "Towarowa 15", "04-08-18",  "09:20"),
                                 ("Małgorzata Kowalska", "Jaskólska 2", "08-07-18",  "09:00"),
                                 ("Edmund Nowak", "Jaskólska 2", "15-06-18",  "08:40"),
                                 ("Edmund Nowak", "Jaskólska 2", "10-06-18",  "09:00"),
                                 ("Piotr Rojek", "Towarowa 15", "12-03-18",  "09:20"),
                                 ("Alicja Konstantynowicz", "Janowicza 5", "07-02-18",  "08:00"),
                                 ("Alicja Konstantynowicz", "Janowicza 5", "04-02-18",  "10:00")]
        self.upcoming_visits = []

# Visit with its most important information
#class Visit:
    #def __init__(self, doctor, day, hour, place):
     #   self.doctor = doctor
      #  self.day = day
       # self.hour = hour
        #self.place = place



