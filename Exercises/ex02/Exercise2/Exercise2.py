def histogram_length(file_path):
    lines = sc.textFile(file_path)
    filt_lines = lines.filter(lambda x: x != '')
    
    split_lines = filt_lines.flatMap(lambda x: x.split(' '))
    wordLearn_lines = split_lines.map(lambda x: (len(x), x))
    lenAndTimes = wordLearn_lines.map(lambda x: (x[0], 1))
    
    shuff_lines = lenAndTimes.groupByKey().map(lambda x: (x[0], list(x[1])))
    
    reduce_times_lines = shuff_lines.map(lambda x: (x[0], reduce(lambda x, y: x + y, x[1])))
    
    output = reduce_times_lines.sortBy(lambda x: x[0])
    
    final_out = output.filter(lambda x: 0 < x[0] < 17)
    return final_out.collect()
    
histogram_length("data/quixote.txt")





(x_values, y_values) = zip(*length_quixote[:10])
plt.bar(x_values, y_values)
plt.title('Histogram of repetitions (up to 10)')
plt.xlabel('Number of repetitions')
plt.ylabel('Number of words')
plt.show()




