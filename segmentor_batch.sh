echo "请输入切词处理开始的标签数："
read begin
echo "请输入切词处理结束的标签数："
read end

for((label=$begin;label<=$end;label++))  
do
	echo "正在对标签数为$label的文本进行切词操作"
	./segmentor.sh sogou_seg_dict_cleaned.txt $label'd'.txt $label'dd'.txt true
done
echo "Finished"
