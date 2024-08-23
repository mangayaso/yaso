import time

while 1:
    with open('test_deploy_text', 'a') as f:
        f.write('test '+f'{time.time()}\n')
    time.sleep(60)
    print(1)

