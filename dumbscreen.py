from generate_trials import trials, generate_stim, regular_poly, GPIO, pygame, np
import pendulum
import csv
import sys
import random


def main():
    # GPIO setup
    short_pin = 17
    long_pin = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(short_pin, GPIO.OUT)
    GPIO.setup(long_pin, GPIO.OUT)

    # PyGame setup
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    points = regular_poly(8, 400, 240, 170)

    # Flags
    pos_undecided = True

    while True:
        if pos_undecided:
            pos_a, pos_b = random.sample(points, 2)
            pos_undecided = False

        short_btn = pygame.draw.circle(screen, (236, 245, 66), pos_a, 50) # yellow
        long_btn = pygame.draw.circle(screen, (174, 2, 242), pos_b, 50) # purple
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if short_btn.collidepoint(pos):
                    GPIO.output(short_pin, GPIO.HIGH)
                    screen.fill("black")
                    pygame.display.flip()
                    pygame.time.delay(200)
                    GPIO.output(short_pin, GPIO.LOW)
                    pos_undecided = True

                elif long_btn.collidepoint(pos):
                    GPIO.output(long_pin, GPIO.HIGH)
                    screen.fill("black")
                    pygame.display.flip()
                    pygame.time.delay(200)
                    GPIO.output(long_pin, GPIO.LOW)
                    pos_undecided = True

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    finally:
        GPIO.cleanup()
