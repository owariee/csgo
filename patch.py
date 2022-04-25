#!/usr/bin/env python3

class Config:
    def __init__(self, path):
        command_list = []
        file = open(path, "r")
        for line in file:
            command_list.append(Command(line))
        
        self.__command_list = command_list
        self.__command_list_length = len(command_list)
    
    def getCommand(self, index):
        command = None
        if(self.getCommandLength() > index):
            command = self.__command_list[index] 
        return command
    
    def setCommand(self, index, command):
        self.__command_list[index] = command

    def appendCommand(self, command):
        self.__command_list.append(command)
        self.__command_list_length = len(self.__command_list)

    def getCommandLength(self):
        return self.__command_list_length
    
    def getCommandList(self):
        return self.__command_list

    def print(self):
        for command in self.getCommandList():
            command.print()

    def merge(self, config):
        unused_commands_index = list(range(config.getCommandLength()))
        for self_command_index in range(self.getCommandLength()):
            self_command = self.getCommand(self_command_index)
            for other_command_index in range(config.getCommandLength()):
                other_command = config.getCommand(other_command_index)
                if(self_command.areEqual(other_command) and other_command_index in unused_commands_index):

                    if(other_command.getCommand() == "zoom_sensitivity_ratio_mouse"):
                        print("cringe")
                    
                    self.setCommand(self_command_index, other_command)
                    unused_commands_index.remove(other_command_index-1)
                    break
        for unused_command_index in unused_commands_index:
            unused_command = config.getCommand(unused_command_index)
            if(unused_command.isValid() and not unused_command.isComment()):
                self.appendCommand(unused_command)
    
    def save(self, path):
        file = open(path, "x")
        for command in self.getCommandList():
            file.write(command.getFullCommand())
    
    def sort(self):
        commandLength = self.getCommandLength()
        for first_index in range(commandLength-1):
            for second_index in range(first_index+1, commandLength):
                first_command = self.getCommand(first_index)
                second_command = self.getCommand(second_index)
                if(second_command.getFullCommand() < first_command.getFullCommand()):
                    self.setCommand(first_index, second_command)
                    self.setCommand(second_index, first_command)

class Command:
    def __init__(self, line):
        parameters = []
        for i in line.strip().split():
            parameters.append(i.strip())
        parameters_length = len(parameters)

        if(parameters_length < 1):
            command = ""
        else:
            command = parameters[0]

        if(parameters_length < 2):
            arguments = []
        else:
            arguments = parameters[1:]

        self.__command = command
        self.__command_length = len(command)
        self.__arguments = arguments
        self.__arguments_length = len(arguments)
    
    def isComment(self):
        return self.isValid() and self.__command[0] == '/' and self.__command[1] == '/'

    def isValid(self):
        return self.__command_length > 1

    def getArgumentLength(self):
        return self.__arguments_length

    def getArgument(self, index):
        argument = None
        if(self.getArgumentLength() > index):
            argument = self.__arguments[index]
        return argument
    
    def getCommand(self):
        return self.__command
    
    def print(self):
        if(self.isValid()):
            print("---\nCommand: {}".format(self.getCommand()))
            print("Is comment: {}".format(self.isComment()))
            for i in range(self.getArgumentLength()):
                print("Argument #{}: {}".format(i, self.getArgument(i)))
        else:
            print("---\nInvalid Command!")
    
    def areEqual(self, command):
        areEqual = False
        if(self.isValid() and command.isValid() and
           not self.isComment() and not command.isComment() and
           self.getArgumentLength() == command.getArgumentLength() and
           self.getCommand() == command.getCommand()):
            if(self.getArgumentLength() == 2 and self.getArgument(0) == command.getArgument(0)):
                areEqual = True
            if(self.getArgumentLength() == 1):
                areEqual = True
        return areEqual
    
    def getFullCommand(self):
        full_command = ""
        if(self.isValid()):
            full_command += self.getCommand()
            for argument_index in range(self.getArgumentLength()):
                argument = self.getArgument(argument_index)
                full_command += " " + argument
        full_command += "\n"
        return full_command

def main():
    vanilla = Config("vanilla/config.cfg")
    patch = Config("autoexec.cfg")
    vanilla.merge(patch)
    vanilla.sort()
    vanilla.save("teste.cfg")

if(__name__ == '__main__'):
    main()
