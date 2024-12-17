# Initial list of provinces
province = ["กรุงเทพมหานคร", "กาฬสินธุ์", "กาญจนบุรี", "จันทบุรี", "ฉะเชิงเทรา", "ชลบุรี", "พะเยา", "ชุมพร", 
            "ชัยนาท", "ขอนแก่น", "ชัยภูมิ", "ยโสธร", "นครพนม", "นครราชสีมา", "เชียงใหม่"]

# Replace specific values in the list
province[province.index("กรุงเทพมหานคร")] = "Bangkok"
province[province.index("นครราชสีมา")] = "Korat"
province[province.index("ฉะเชิงเทรา")] = "Paet Riw"
province[province.index("ชลบุรี")] = "Chon buri"
province[province.index("ชุมพร")] = "Chum porn"

# Print the updated list
print(province)