import asyncio
from pydngconverter import DNGConverter , flags



async def main():
    inputPath = input("Select Source File Path: ")
    print("Input Path: ", inputPath)
    outputPath = input("Select Destenation File Path: ")
    print("Output Path: ", outputPath)

    pydng = DNGConverter(inputPath, dest=outputPath, jpeg_previews = flags.JPEGPreview.EXTRACT, fast_load = True,)


    return await pydng.convert()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()