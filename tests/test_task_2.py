from task_2 import  go_to_images


def test_image(test):
    driver.switch_to.window(driver.window_handles[1])
    if test == driver.current_window_handle:
        print(f'Окна совпадают: {driver.current_window_handle}')
        time.sleep(300)
    else:
        print('Окна не  совпадают')
