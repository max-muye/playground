#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

// 画布类
class Canvas {
private:
    vector<vector<char>> grid;
    int width, height;
    int cursorX, cursorY;
    char brushChar;

public:
    Canvas(int w, int h) : width(w), height(h), cursorX(0), cursorY(0), brushChar('*') {
        grid.resize(height, vector<char>(width, ' '));
    }

    // 清屏函数
    void clearScreen() {
        system("clear");
    }

    // 绘制画布
    void draw() {
        clearScreen();
        cout << "=== C++ 画笔程序 ===" << endl;
        cout << "画笔字符: " << brushChar << " | 位置: (" << cursorX << "," << cursorY << ")" << endl;
        cout << "操作: W/A/S/D移动 | 空格键绘制 | C清屏 | Q退出 | 1-9选择画笔字符" << endl;
        cout << string(width + 2, '=') << endl;
        
        for (int i = 0; i < height; i++) {
            cout << "|";
            for (int j = 0; j < width; j++) {
                if (i == cursorY && j == cursorX) {
                    cout << "\033[31m@\033[0m"; // 红色光标
                } else {
                    cout << grid[i][j];
                }
            }
            cout << "|" << endl;
        }
        cout << string(width + 2, '=') << endl;
    }

    // 移动光标
    void moveCursor(int dx, int dy) {
        int newX = cursorX + dx;
        int newY = cursorY + dy;
        
        if (newX >= 0 && newX < width && newY >= 0 && newY < height) {
            cursorX = newX;
            cursorY = newY;
        }
    }

    // 在当前位置绘制
    void drawAtCursor() {
        grid[cursorY][cursorX] = brushChar;
    }

    // 清空画布
    void clear() {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                grid[i][j] = ' ';
            }
        }
    }

    // 设置画笔字符
    void setBrushChar(char c) {
        brushChar = c;
    }

    // 获取用户输入
    char getInput() {
        cout << "请输入操作 (W/A/S/D移动, 空格绘制, C清屏, Q退出, 1-9选择画笔): ";
        char input;
        cin >> input;
        return input;
    }
};

int main() {
    cout << "欢迎使用C++画笔程序！" << endl;
    cout << "正在初始化画布..." << endl;
    
    Canvas canvas(20, 10); // 20x10的画布
    bool running = true;
    
    cout << "画布已创建！按回车键开始..." << endl;
    cin.get();
    
    while (running) {
        canvas.draw();
        
        char input = canvas.getInput();
        switch (input) {
            case 'w':
            case 'W':
                canvas.moveCursor(0, -1);
                break;
            case 's':
            case 'S':
                canvas.moveCursor(0, 1);
                break;
            case 'a':
            case 'A':
                canvas.moveCursor(-1, 0);
                break;
            case 'd':
            case 'D':
                canvas.moveCursor(1, 0);
                break;
            case ' ': // 空格键绘制
                canvas.drawAtCursor();
                break;
            case 'c':
            case 'C':
                canvas.clear();
                break;
            case 'q':
            case 'Q':
                running = false;
                break;
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                canvas.setBrushChar(input);
                break;
            default:
                cout << "无效输入，请重试！" << endl;
                break;
        }
    }
    
    cout << "感谢使用C++画笔程序！" << endl;
    return 0;
} 