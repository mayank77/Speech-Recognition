a = zeros(1,6);
b = zeros(1,6);
class = zeros(1,6);
iterate = 1;
start = 25;
endd = 50;
for count = start:endd
S = train_gmm(train_data, train_class, count);
result = gmmb_decide(gmmb_normalize(gmmb_pdf(train_data, S)));
result1 = gmmb_decide(gmmb_normalize(gmmb_pdf(test_data, S)));
a(iterate) = length(find(result~=train_class))/length(train_class)*100;
b(iterate) = length(find(result1~=test_class))/length(test_class)*100;
class(iterate) = count;
iterate = iterate + 1;
end

plot(class,a)
hold on
plot(class,b)
hold off