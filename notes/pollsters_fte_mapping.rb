require "csv"

types = ["", "FteName", "ShortName", "Name2014", "HuffpostName", "DailyKosName", "CopyeditedName"]
types.each do |type|
	puts type
	CSV.open("_" + type + ".csv", "wb") do |csv|
		PollsterName.includes(:pollster).where(:type => type).each do |p|
			csv << [p.name, p.pollster ? p.pollster.name : ""]
		end
	end
end

# CSV.open("fte_pollster_mapping.csv", "wb") do |csv|
# 	Pollster.all.each do |p|
# 		p.pollster_names.select {}
# 	end
#   csv << ["animal", "count", "price"]
#   csv << ["fox", "1", "$90.00"]
# end
