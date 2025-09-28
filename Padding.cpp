void printCentered(string text, int width = 80) {
    int padding = (width - text.length()) / 2;

    if (padding < 0) 
        padding = 0;

    cout << string(padding, ' ') << text << endl;
}
