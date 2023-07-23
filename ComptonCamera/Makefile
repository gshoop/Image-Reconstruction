# Compiler
CXX = g++

# Header directory
HEADER_DIR = Headers

# Source directory
SOURCE_DIR = Source

# Object files
OBJECTS = $(SOURCE_DIR)/ccFunctions.o $(SOURCE_DIR)/ccRecon.o

# Executable
TARGET = recon

# Rules
all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) -o $(TARGET) $(OBJECTS)

ccFunctions.o: $(HEADER_DIR)/ccFunctions.h
	$(CXX) -c $(SOURCE_DIR)/ccFunctions.cpp

ccRecon.o: $(HEADER_DIR)/ccFunctions.h
	$(CXX) -c $(SOURCE_DIR)/ccRecon.cpp

clean:
	rm -f $(OBJECTS) $(TARGET)