import logging as lg


def algo_log(filename=None):
    if filename is None:
        filename = "algo_demo.log"
    lg.basicConfig(filename=filename, encoding="utf-8", level=lg.DEBUG,
                   format="%(asctime)s %(name)s %(levelname)s %(message)s")
    return
