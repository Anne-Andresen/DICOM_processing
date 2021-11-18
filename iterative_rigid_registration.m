
for i=01:65
    if i <= 9 
        path= ['D:/test/h/ScalarVolume_12/IMG000' num2str(i) '.dcm']
    else
        path = ['D:/test/h/ScalarVolume_12/IMG00' num2str(i) '.dcm']
    end
    
    [filepath,name,ext] = fileparts(path)
    fixed = dicomread(['D:/test/h/ScalarVolume_12/' name '.dcm']);
    moving = dicomread(['D:/test/ScalarVolume_7/' name '.dcm']);
    % imshowpair(fixed, moving,'Scaling','joint')
   % title('Before Rigid transform')
    [optimizer, metric] = imregconfig('multimodal')
    optimizer.InitialRadius = 0.009;
    optimizer.Epsilon = 1.5e-4;
    optimizer.GrowthFactor = 1.00000000001;
    optimizer.MaximumIterations = 300;
    movingRegistered = imregister(moving, fixed, 'rigid', optimizer, metric);
    %figure
    %imshowpair(fixed, movingRegistered,'Scaling','joint')
    X = ['D:/test/h/' name '.dcm']
    dicomwrite(movingRegistered, X)
    %title('After Rigid transform');

end
