import os
from colorama import Fore, Style
from helper import cli
import numpy as np
import cv2

def main():
	
	message = ""
	while True:
		# cli.clear()
		print("WATERMARK TOOLS")
	
		if message != "":
			print(message)

		imgpath = input("Enter image location : ").strip()
		
		# Validate input cannot be empty
		if imgpath == "":
			message = Fore.RED + "Image location cannot be empty." + Style.RESET_ALL
			continue
		
		# Validate input is a valid path
		if not os.path.exists(imgpath):
			message = Fore.RED + "Image location does not exist." + Style.RESET_ALL
			continue
		
		watermarktext = input("Enter watermark text : ").strip()
		if watermarktext == "":
			message = Fore.RED + "Watermark text cannot be empty." + Style.RESET_ALL
			continue
		
		image = cv2.imread(imgpath)
		overlay = image.copy()
		font = cv2.FONT_HERSHEY_PLAIN
		font_scale = 1.5

		image_height, image_width = image.shape[:2]
		(text_width, text_height), baseline = cv2.getTextSize(
			watermarktext, font, font_scale, 1
		)

		padding_x = 20
		padding_y = 20
		alpha = 0.3
		
		for iy, y in enumerate(range(0, image_height, text_height + padding_y)):
			for ix, x in enumerate(range(0, image_width, text_width + padding_x)):

				if iy % 2 == 0:
					x = x - text_width // 2				

				cv2.putText(
					overlay,
					watermarktext,
					(x, y + text_height + padding_y // 2),
					font,
					font_scale,
					(255, 255, 255),
					1,
				)	 
				

		cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
		cv2.imshow("Watermark", image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
main()