addpath /work/courses/T/S/89/5150/general/ex1/
addpath /work/courses/T/S/89/5150/general/ex1/gmmbayestb
load ex1data
plot(sampleword)

s = spectrogram(sampleword, hamming(400), 240); % 32000*0.025s/2s=400 , 400-16khzx10ms = 240)
imagesc(sqrt(abs(s)))
axis xy
sample_word_segmentation

s2 = spectrogram(filter([1 -0.97], 1, sampleword), hamming(400), 240);
figure
imagesc(sqrt(abs(s2)))
axis xy
sample_word_segmentation

plot(M', 'b')

figure
imagesc(log(M*sqrt(abs(s2))+1))
axis xy
sample_word_segmentation

imagesc(D)
colorbar

figure
imagesc(D*log(M*sqrt(abs(s2))+1))
axis xy
sample_word_segmentation