def main():
    print("Fake web framework")

    try:
        text = input("Do you want to redirect or see the page? [y/n] ")
        if text == 'y':
            redirect_to_v1('https://talkpython.fm')
            print("We are redirecting the user...")

        print("You see the page content and are amazed!")
    except HTTPException as x:
        print(f"Framework redirect exception: {x}")
    except ValueError:
        print("Framework: 400 bad request")


# region Exceptions...
class HTTPException(Exception): ...


class HTTPFound(HTTPException): ...


class HTTPMovedPermanently(HTTPException): ...


# endregion

def redirect_to_v1(url, permanent=False) -> None:
    if not url:
        raise ValueError('url')

    if permanent:
        raise HTTPMovedPermanently(url)

    raise HTTPFound(url)


if __name__ == '__main__':
    main()
