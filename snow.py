# 1. opencv, numpy 라이브러리 가져오기


# 2. face 분류기 로드 & 가면 영상 불러오기



if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')
cap = cv2.VideoCapture("test1.mp4")
scaling_factor = 0.5

# 3. 동영상 읽고 처리하기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # 4. Frame을 gray영상으로 만들고 face 분류기를 로드하기
   
    # 5. 검출된 얼굴에 마스크 합성하기

            # frame 얼굴에 맞춰서 자르기
            
            
            # 검출된 얼굴의 크기와 같도록 마스크의 크기 조절
           cv2.imshow('gray_mask', gray_mask)

           cv2.imshow('thresholding_mask', mask)
        # 6. mask에 bitwise_not연산자를 사용하여 흑백을 바꾸어준다.
        #     masked_frame에 mask를 적용한 얼굴 프레임이 들어간다.

        
        cv2.imshow('Face mask_inv', mask_inv)

        
        cv2.imshow('masked_face', img2)
        
    
    cv2.imshow('Face Detector', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

      