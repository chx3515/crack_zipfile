import zipfile


def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd=bytes(password, 'utf8'))
        print("李大伟的压缩包密码是%s" % password)
        return True
    except:
        pass


def main():
    zipFile = zipfile.ZipFile('README.zip')
    PwdLists = open('passdict.txt')
    for line in PwdLists.readlines():
        pwd = line.strip('\n')
        guess = extractFile(zipFile, pwd)
        if guess:
            break


if __name__ == '__main__':
    main()
