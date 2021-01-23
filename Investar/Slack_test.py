from slacker import Slacker
slack = Slacker("xoxb-1451409102051-1457744755044-RaFnnJmTgggJ0lANu2UMbSak")

markdown ='''
          This message is plain. 
          *This message is bold.* 
          'This message is code'
          _This message is italic_
          ~This message is strike.~
          '''

attach_dict = {
    'color' :   "#ff0000",
    "author_name": "Sean",
    "author_link":"https://github.com/LeeDong-Min",
    "title" : "오늘의 증시 KOSPI",
    "title_link": "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI",
    "text" : "3092.66 Δ78.73(+2.61%)",
    "image_url" : "https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png"
}
attach_list = [attach_dict]
slack.chat.post_message("study", text=markdown,attachments=attach_list)
