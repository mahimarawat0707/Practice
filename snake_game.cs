// Program.cs
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

namespace SnakeGame
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            ApplicationConfiguration.Initialize(); // .NET 6+ WinForms helper
            Application.Run(new SnakeForm());
        }
    }

    public class SnakeForm : Form
    {
        private enum Direction { Up, Down, Left, Right }

        private readonly Timer gameTimer = new Timer();
        private readonly List<Point> snake = new List<Point>();
        private Point food;
        private Direction currentDirection = Direction.Right;
        private Direction nextDirection = Direction.Right;
        private readonly Random rnd = new Random();
        private int score = 0;

        // Config
        private const int CellSize = 20;
        private const int GridWidth = 30;  // total width in cells
        private const int GridHeight = 20; // total height in cells
        private const int InitialSnakeLength = 5;
        private const int TimerIntervalMs = 100; // lower = faster

        private bool gameOver = false;

        public SnakeForm()
        {
            Text = "Snake - C#";
            ClientSize = new Size(GridWidth * CellSize, GridHeight * CellSize + 30);
            DoubleBuffered = true;

            StartPosition = FormStartPosition.CenterScreen;
            KeyDown += OnKeyDown;
            Paint += OnPaint;

            InitializeGame();

            gameTimer.Interval = TimerIntervalMs;
            gameTimer.Tick += GameTick;
            gameTimer.Start();
        }

        private void InitializeGame()
        {
            snake.Clear();
            int startX = GridWidth / 2;
            int startY = GridHeight / 2;

            for (int i = 0; i < InitialSnakeLength; i++)
            {
                // Start horizontal to the left
                snake.Add(new Point(startX - i, startY));
            }

            currentDirection = nextDirection = Direction.Right;
            score = 0;
            gameOver = false;

            PlaceFood();
            Invalidate();
        }

        private void PlaceFood()
        {
            while (true)
            {
                int x = rnd.Next(0, GridWidth);
                int y = rnd.Next(0, GridHeight);
                Point candidate = new Point(x, y);
                if (!snake.Contains(candidate))
                {
                    food = candidate;
                    return;
                }
            }
        }

        private void GameTick(object? sender, EventArgs e)
        {
            if (gameOver) return;

            // Accept nextDirection but disallow immediate 180-degree turn
            if (!IsOpposite(nextDirection, currentDirection))
                currentDirection = nextDirection;

            Point head = snake[0];
            Point newHead = head;

            switch (currentDirection)
            {
                case Direction.Up: newHead = new Point(head.X, head.Y - 1); break;
                case Direction.Down: newHead = new Point(head.X, head.Y + 1); break;
                case Direction.Left: newHead = new Point(head.X - 1, head.Y); break;
                case Direction.Right: newHead = new Point(head.X + 1, head.Y); break;
            }

            // Check wall collision
            if (newHead.X < 0 || newHead.X >= GridWidth || newHead.Y < 0 || newHead.Y >= GridHeight)
            {
                EndGame();
                return;
            }

            // Check self collision
            if (snake.Contains(newHead))
            {
                EndGame();
                return;
            }

            // Move snake
            snake.Insert(0, newHead);

            // Eating food?
            if (newHead == food)
            {
                score += 10;
                PlaceFood();
            }
            else
            {
                // remove tail
                snake.RemoveAt(snake.Count - 1);
            }

            Invalidate(); // redraw
        }

        private static bool IsOpposite(Direction a, Direction b)
        {
            return (a == Direction.Up && b == Direction.Down) ||
                   (a == Direction.Down && b == Direction.Up) ||
                   (a == Direction.Left && b == Direction.Right) ||
                   (a == Direction.Right && b == Direction.Left);
        }

        private void EndGame()
        {
            gameOver = true;
            gameTimer.Stop();
            Invalidate();
        }

        private void OnKeyDown(object? sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Up || e.KeyCode == Keys.W)
                nextDirection = Direction.Up;
            else if (e.KeyCode == Keys.Down || e.KeyCode == Keys.S)
                nextDirection = Direction.Down;
            else if (e.KeyCode == Keys.Left || e.KeyCode == Keys.A)
                nextDirection = Direction.Left;
            else if (e.KeyCode == Keys.Right || e.KeyCode == Keys.D)
                nextDirection = Direction.Right;
            else if (e.KeyCode == Keys.Space)
            {
                if (gameOver)
                {
                    InitializeGame();
                    gameTimer.Start();
                }
            }
            else if (e.KeyCode == Keys.Escape)
            {
                Close();
            }
        }

        private void OnPaint(object? sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;

            // background
            g.Clear(Color.FromArgb(30, 30, 30));

            // draw grid (optional subtle grid)
            using (Pen gridPen = new Pen(Color.FromArgb(50, 50, 50)))
            {
                for (int x = 0; x <= GridWidth; x++)
                {
                    g.DrawLine(gridPen, x * CellSize, 0, x * CellSize, GridHeight * CellSize);
                }
                for (int y = 0; y <= GridHeight; y++)
                {
                    g.DrawLine(gridPen, 0, y * CellSize, GridWidth * CellSize, y * CellSize);
                }
            }

            // draw food
            Rectangle foodRect = new Rectangle(food.X * CellSize + 2, food.Y * CellSize + 2, CellSize - 4, CellSize - 4);
            using (Brush fb = new SolidBrush(Color.Red))
            {
                g.FillEllipse(fb, foodRect);
            }

            // draw snake
            for (int i = 0; i < snake.Count; i++)
            {
                Point p = snake[i];
                Rectangle r = new Rectangle(p.X * CellSize + 1, p.Y * CellSize + 1, CellSize - 2, CellSize - 2);

                if (i == 0)
                {
                    // head
                    using (Brush hb = new SolidBrush(Color.FromArgb(50, 205, 50)))
                    using (Pen outline = new Pen(Color.FromArgb(20, 20, 20), 2))
                    {
                        g.FillRectangle(hb, r);
                        g.DrawRectangle(outline, r);
                    }
                }
                else
                {
                    // body
                    using (Brush bb = new SolidBrush(Color.FromArgb(34, 139, 34)))
                    {
                        g.FillRectangle(bb, r);
                    }
                }
            }

            // draw score
            string scoreText = $"Score: {score}  Length: {snake.Count}";
            using (Font f = new Font("Segoe UI", 10, FontStyle.Bold))
            using (Brush textBrush = new SolidBrush(Color.White))
            {
                g.DrawString(scoreText, f, textBrush, new PointF(6, GridHeight * CellSize + 6));
            }

            // game over message
            if (gameOver)
            {
                string msg = "Game Over! Press SPACE to restart";
                using (Font big = new Font("Segoe UI", 16, FontStyle.Bold))
                using (Brush b = new SolidBrush(Color.Yellow))
                {
                    SizeF ms = g.MeasureString(msg, big);
                    float x = (ClientSize.Width - ms.Width) / 2;
                    float y = (ClientSize.Height - ms.Height) / 2 - 20;
                    g.DrawString(msg, big, b, x, y);
                }
            }
        }
    }
}
