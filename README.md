# DICOM processing

MATLAB code for iterative rigid registratio of DICOM MRI files in 2D, can also be changed to affined, similar and transform

Including visualization of before:

<img width="477" alt="reg_rigid_before" src="https://user-images.githubusercontent.com/56411446/142409633-8d630924-2f2f-49c5-a85a-d6d5f4fc9229.png">

And visualization of after registration:

<img width="430" alt="reg_rigid_After" src="https://user-images.githubusercontent.com/56411446/142409736-decaa41e-7a76-4fe8-830b-1f829c091bec.png">

The final img becomes a gray scale img  without shadows which is registered to the fixes domain, and is saved on the same name as the original non registered img in DICOM format


Futher this resposityr inludes an interative dicom to png converter in python, with intensity normalization, to obtain intensity normalized png files,can likewise be used for intensity normalizing DICOM images

If codes is used please do cite. 
Feel free to start an issue if there is any problem with the code, im happy to help. 




