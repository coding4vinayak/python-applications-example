from watermark import File, Watermark, apply_watermark, Position

image = File("wtr.pdf")

watermark = Watermark(File("super.pdf"), pos =Position.bottom_right )

apply_watermark(image,watermark)
