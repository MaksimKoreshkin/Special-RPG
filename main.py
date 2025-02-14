# -*- coding: utf-8 -*-
from rich.console import Console
from modules.text import *
import modules.entity as entity
import os
import sys
import time
import modules.items as items
from modules.settings import *

# Init console object
console = Console()

# Init global variables
LOGO = """
\x1b[37;1m███████████████████████████████████████████████████████████████████████\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[36;1m┏━━━━━━━━━━━┓\x1b[;0m          \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┏━━━━━━━━━━━┓ \x1b[;0m \x1B[35;1m┏━━━━━━━━━━┓\x1b[;0m \x1B[35;1m┏━━━━━━━━━━━┓\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[36;1m┃  ┏━━━━━━━━┛\x1b[;0m          \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┏━━━━┓  ┃ \x1b[;0m \x1B[35;1m┃   ┏━━━━┓ ┃\x1b[;0m \x1B[35;1m┃  ┏━━━━━━━━┛\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[36;1m┃  ┗━━━━━━━━┓\x1b[;0m  ┏━━━━┓  \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┗━━━━┛  ┃ \x1b[;0m \x1B[35;1m┃   ┗━━━━┛ ┃\x1b[;0m \x1B[35;1m┃  ┃         \x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[36;1m┗━━━━━━━━━┓ ┃\x1b[;0m  ┃ ██ ┃  \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ━━━━━━┳━┛ \x1b[;0m \x1B[35;1m┃  ┏━━━━━━━┛\x1b[;0m \x1B[35;1m┃  ┃  ┏━━━━━┓\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[36;1m┏━━━━━━━━━┛ ┃\x1b[;0m  ┗━━━━┛  \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┏━━━┓ ┗━━┓\x1b[;0m \x1B[35;1m┃  ┃        \x1b[;0m \x1B[35;1m┃  ┃  ┗━━━┓ ┃\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m \x1B[36;1m┗━━━━━━━━━━━┛\x1b[;0m          \x1b[37;0m┃\x1b[;0m  \x1B[31;1m┃   ┃   ┗━┓  ┃\x1b[;0m \x1B[35;1m┃  ┃        \x1b[;0m \x1B[35;1m┃  ┗━━━━━━┛ ┃\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m█\x1b[;0m ━━━━━━━━━━━━━          ┃  \x1B[31;1m┗━━━┛     ┗━━┛\x1b[;0m \x1B[35;1m┗━━┛         \x1b[;0m\x1B[35;1m┗━━━━━━━━━━━┛\x1b[;0m \x1b[37;1m█\x1b[;0m
\x1b[37;1m███████████████████████████████████████████████████████████████████████\x1b[;0m"""
# Commands
NEW      = 'new'
LOAD     = 'load'
LAST     = 'last'
SETTINGS = 'settings'
EXIT     = 'exit'
INV = 'inv'
THINK = 'think'
GO = 'go'
TALK = 'talk'
TAKE = 'take'
PUTE = 'put'
CRAFT = 'craft'
# Settings commands
SET = 'set'
DEF = 'def'
DEFALL = 'defall'
text_delay = float(settings['delay'][1])
class Game:
    def initialition_save(self):
        # Init main menu
        self.main_menu_context = {
            NEW:('Новое сохранение',self.new),
            LOAD:('Загрузить сохранение',self.load),
            LAST:('Последние сохранение',self.last),
            SETTINGS:('Настройки',self.settings),
            EXIT:('Выход на рабочий стол',self.exit)
        }
        self.settings_menu_context = {
            SET:('Изменить значение настройки (set <название> <значение>)',),
            DEF:('Изменить значение настройки по умолчанию (def <название>)',),
            DEFALL:('Сбросить всё по умолчанию (defall)',),
            EXIT:('Выход в главное меню (exit)',)
        }
        print(LOGO) # Print a logo
        add(LOGO) # Add to untimed
        print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
        add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
        self.agreetisment() # Show title welcome
        print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
        add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
        self.menu() # Show all menu
        special_print('Введите название команды', color='\x1B[35;1m', _add=True)
        # Set lambdas
        self.l_in_commands = lambda choice: choice.lower().rstrip() in self.main_menu_context.keys()
        self.l_no_params = lambda choice: len(choice.split(' ')) == 1
        self.l_params = lambda choice: len(choice.split(' ')) == 2
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            # If choice in commands
            if self.l_in_commands(choice.split(' ')[0]):
                # If in command no parameters
                if self.l_no_params(choice):
                    # print(' '*(INSIDE_TEXT_SIZE-len('-~> '+choice)-1)+'\x1B[37;1m█\x1B[0m')
                    debug(f'Invoked: {choice.lower().rstrip()}')
                    s = self.main_menu_context[choice.lower().rstrip()][1]() # Invoke command
                    if choice.lower().rstrip() == NEW:
                        return s
                else:
                    special_print('Ошибка! Эта функция вызывается без параметров!', color='\x1B[31;1m', delay=0.01)
                    time.sleep(len('Ошибка! Эта функция вызывается без параметров!')/50)
                    redrow()
            else:
                special_print('Неизвестная команда!', '\x1B31[;1m')
                time.sleep(len('Неизвестная команда!')/50)
                redrow()

        print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
        add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
        print('\x1B[37;1m███████████████████████████████████████████████████████████████████████\x1b[;0m') # Print a full line
        add('\x1B[37;1m███████████████████████████████████████████████████████████████████████\x1b[;0m')

    # Commands functions
    def new(self):
        special_print('Введите имя персонажа', '\x1B37[;1m')
        print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
        player_name = input()
        
        self.player = entity.Player(
            name=player_name,
            hp=10,
            items=[items.test_item],
            description='Разборщик, пайщик, разбирается в электронике',
            interesting='?'
        )
        self.save = Save(self.player, "sadasd")
        return self.save
        
    def load(self):
        print('load')
    def last(self):
        print('last')
    def settings(self):
        global settings
        del untimed_text[2:-1]
        redrow()
        self.settings_menu_commands()
        special_print('Настройки', '\x1B[37;1m')
        self.settings_menu()
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            # If choice in commands
            if choice.lower().split(' ')[0] in self.settings_menu_context.keys():
                if choice.lower().split(' ')[0] == SET:
                    if len(choice.lower().split(' ')) == 3:
                        option_name = choice.lower().split(' ')[1]
                        arg = choice.lower().split(' ')[2]
                        if option_name in settings.keys():
                            if settings_cheacking_funcs[option_name](arg): # Invoke cheack function
                                settings[option_name][1] = arg
                                update_settings()
                                special_print('Изменено', color='\x1B[33;1m')
                                time.sleep(len('Изменено')/50)
                                redrow()
                                special_print('Настройки', '\x1B[37;1m')
                                self.settings_menu2()
                            else:
                                special_print('Ошибка! Неверный параметр', color='\x1B[31;1m', delay=0.01)
                                time.sleep(len('Ошибка! Неверный параметр')/50)
                                redrow()
                                special_print('Настройки', '\x1B[37;1m')
                                self.settings_menu2()
                        else:
                            special_print('Ошибка! Неизвестная настройка', color='\x1B[31;1m', delay=0.01)
                            time.sleep(len('Ошибка! Неизвестная настройка')/50)
                            redrow()
                            self.settings_menu2()
                elif choice.lower().rstrip() == EXIT:
                    del untimed_text[1:7]
                    redrow()
                    print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
                    add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
                    self.agreetisment() # Show title welcome
                    print(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m') # Print an emtpy line
                    add(f'\x1B[37;1m█{INSIDE_TEXT_GAP}█\x1b[;0m')
                    self.menu() # Show all menu
                    special_print('Введите название команды', color='\x1B[35;1m', _add=True)
                    break
                    
                elif choice.lower().split(' ')[0] == DEF:
                    if len(choice.lower().split(' ')) == 2:
                        option_name = choice.lower().split(' ')[1]
                        if option_name in settings.keys():
                            settings[option_name] = default_settings[option_name]
                            update_settings()
                            special_print('Изменено', color='\x1B[33;1m')
                            time.sleep(len('Изменено')/50)
                            redrow()
                        else:
                            special_print('Ошибка! Неизвестная настройка', color='\x1B[31;1m', delay=0.01)
                            time.sleep(len('Ошибка! Неизвестная настройка')/50)
                            redrow()
                            special_print('Настройки', '\x1B[37;1m')
                            self.settings_menu2()

                elif choice.lower().rstrip() == DEFALL:
                    settings = default_settings
                    update_settings()
                    special_print('Изменено по умолчанию', '\x1B[33;1m')
                    time.sleep(len('Изменено по умолчанию')/30)
                    redrow()
                    special_print('Настройки', '\x1B[37;1m')
                    self.settings_menu2()
            else:
                special_print('Неизвестная команда!', '\x1B31[;1m')
                time.sleep(len('Неизвестная команда!')/30)
                redrow()
                special_print('Настройки', '\x1B[37;1m')
                self.settings_menu2()
    def settings_menu_commands(self):
        for (name, values) in self.settings_menu_context.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.25)
            print(f'\x1B[36;1m{name} - \x1B[;0m', end='')
            delay_print(f'{values[0]}', '\x1B[35;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+values[0])-2)+' \x1B[37;1m█\x1B[0m')
            add('\x1B[37;1m█\x1B[0m '+'\x1B[36;1m'+name+' - '+'\x1B[;0m'+'\x1B[35;1m'+values[0]+'\x1B[;0m'+' '*(INSIDE_TEXT_SIZE-len(name+' - '+values[0])-2)+' \x1B[37;1m█\x1B[0m')

    def settings_menu(self):
        for (name, values) in settings.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.25)
            print(f'\x1B[36;1m{name} - \x1B[;0m', end='')
            delay_print(f'{values[0]} - ', '\x1B[35;1m', end='')
            delay_print(f'{values[1]}', '\x1B[36;1m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+str(values[0])+' - '+str(values[1]))-2)+' \x1B[37;1m█\x1B[0m')

    def settings_menu2(self):
        for (name, values) in settings.items():
            print(f'\x1B[37;1m█\x1B[0m ', end='')
            time.sleep(0.25)
            print(f'\x1B[36;1m{name} - \x1B[;0m', end='')
            print(f'\x1B[35;1m{values[0]} - \x1B[;0m', end='')
            print(f'\x1B[36;1m{values[1]}\x1B[;0m', end='')
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+str(values[0])+' - '+str(values[1]))-2)+' \x1B[37;1m█\x1B[0m')

    def exit(self):
        special_print('Вы действительно хотите выйти?y/n', '\x1B32[;1m')
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            if choice.lower().rstrip() == 'y':
                raise KeyboardInterrupt
            elif choice.lower().rstrip() == 'n':
                redrow()

    def agreetisment(self):
        print('\x1B[37;1m█\x1B[0m ', end='')
        delay_print('Добро пожаловать в S', '\x1B[36;1m', end='', delay=text_delay)
        delay_print('R', '\x1B[31;1m', end='', delay=text_delay)
        delay_print('PG', '\x1B[35;1m', end='', delay=text_delay)
        delay_print('!', '\x1B[36;1m', end='', delay=text_delay)
        print(' '*(INSIDE_TEXT_SIZE-len("Добро пожаловать в SRPG!")-1)+'\x1B[37;1m█\x1B[0m')
        add('\x1B[37;1m█\x1B[0m '+'\x1B[36;1mДобро пожаловать в S\x1B[31;1mR\x1B[;0m\x1B[35;1mPG\x1B[;0m\x1B[36;1m!\x1B[;0m'+' '*(INSIDE_TEXT_SIZE-len("Добро пожаловать в SRPG!")-1)+'\x1B[37;1m█\x1B[0m')
    
    def menu(self):
        for (number, context) in self.main_menu_context.items():
            print(f'\x1B[37;1m█\x1B[0m \x1B[36;1m{number} - \x1b[;1m', end='')
            time.sleep(0.25)
            delay_print(context[0], '\x1B[35;1m', end='', delay=text_delay)
            print(' '*(INSIDE_TEXT_SIZE-len(number+' - '+context[0])-1)+'\x1B[37;1m█\x1B[0m')
            add(format_text_gap(f'\x1B[36;1m{number} - \x1b[;0m\x1B[35;1m{context[0]}\x1B[0m')) # Context[0] is command description

# Данные которые нужно сохранять
# Объект игрока
# Локации
# Команды игрока
# inv - инвентарь
# think - посмотреть, что думает герой
# go - перейти в другую локацию
# talk - поговорить
# take - взять предмет
# pute - положить предмет
# craft - скрафтить что-то
# exit - выход в главное меню

class Save:
    def __init__(self, player, locations) -> None:
        # Init attributes
        self.player = player
        self.locations = locations
        # Init menu
        self.params_commands = [GO, TALK, TAKE, PUTE, CRAFT]
        self.no_params_commands = [INV, THINK, EXIT]
        self.menu_context = {
            INV:('Инвентарь',self.inv),
            THINK:('Посмотреть, что думает герой',self.think),
            GO:('Перейти в другую локацию',self.go),
            TALK:('Поговорить',self.talk),
            TAKE:('Взять предмет',self.take),
            PUTE:('Положить предмет',self.pute),
            CRAFT:('Скрафтить что-то',self.craft),
            EXIT:('Выйти в главное меню',self.exit),
        }
        del untimed_text[2:-1]
    
    def main(self):
        redrow()
        # Show menu
        self.menu()
        special_print('Введите название команды', color='\x1B[35;1m', _add=True)
        # Set lambdas
        self.l_in_commands = lambda choice: choice.lower().rstrip() in self.menu_context.keys()
        self.l_no_params = lambda choice: len(choice.split(' ')) == 1
        self.l_params = lambda choice: len(choice.split(' ')) == 2
        while True:
            print('\x1B[37;1m█\x1B[0m \x1B[35;1m-~>\x1B[;0m \x1B[31;1m', end='')
            choice = input()
            print('\x1B[;0m')
            # If choice in commands
            if self.l_in_commands(choice.split(' ')[0]):
                # If in command no parameters
                print(self.l_params(choice), choice.lower().rstrip())
                print(self.l_no_params(choice), choice.split(' ')[0].lower().rstrip())
                if self.l_no_params(choice) and choice.lower().rstrip() in self.no_params_commands:
                    #print(' '*(INSIDE_TEXT_SIZE-len('-~> '+choice)-1)+'\x1B[37;1m█\x1B[0m')
                    debug(f'Invoked: {choice.lower().rstrip()}')
                    self.menu_context[choice.lower().rstrip()][1]() # Invoke command
                elif self.l_params(choice) and choice.split(' ')[0].lower().rstrip() in self.no_params_commands:
                    pass
                elif self.l_no_params(choice) and choice.split(' ')[0].lower().rstrip() in self.params_commands:
                    special_print('Ошибка! Эта функция вызывается с параметрами!', color='\x1B[31;1m', delay=0.01)
                    time.sleep(len('Ошибка! Эта функция вызывается с параметрами!')/50)
                    redrow()
                elif self.l_params(choice) and choice.split(' ')[0].lower().rstrip() in self.no_params_commands:
                    special_print('Ошибка! Эта функция вызывается без параметров!', color='\x1B[31;1m', delay=0.01)
                    time.sleep(len('Ошибка! Эта функция вызывается без параметров!')/50)
                    redrow()
            else:
                special_print('\x1B[31;3mНеизвестная команда!', '\x1B31[;1m')
                time.sleep(len('Неизвестная команда!')/50)
                redrow()

    def inv(self):
        redrow()
        special_print('Ваши вещи:', '\x1B[35;1m')
        for (name, item) in self.player.items.items():
            print(f'\x1B[37;1m█\x1B[0m \x1B[36;1m{name} - \x1b[;1m', end='')
            time.sleep(0.25)
            delay_print(item.description, '\x1B[35;1m', end='', delay=text_delay)
            print(' '*(INSIDE_TEXT_SIZE-len(name+' - '+item.description)-1)+'\x1B[37;1m█\x1B[0m')

    def think(self):
        redrow()
        special_print(self.player.total_think, '\x1B36[;1m')
    def go(self): print('go')
    def talk(self): print('talk')
    def take(self): print('take')
    def pute(self): print('pute')
    def craft(self): print('craft')
    def exit(self): print('exit')


    
    def menu(self):
        for (number, context) in self.menu_context.items():
            print(f'\x1B[37;1m█\x1B[0m \x1B[36;1m{number} - \x1b[;1m', end='')
            time.sleep(0.25)
            delay_print(context[0], '\x1B[35;1m', end='', delay=text_delay)
            print(' '*(INSIDE_TEXT_SIZE-len(number+' - '+context[0])-1)+'\x1B[37;1m█\x1B[0m')
            add(format_text_gap(f'\x1B[36;1m{number} - \x1b[;0m\x1B[35;1m{context[0]}\x1B[0m')) # Context[0] is command description

if __name__ == '__main__':
    game = Game().initialition_save()
    game.main()