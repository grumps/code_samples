// imports removed

public class DashboardTabFragment extends BaseFragment {
    private final String TAG = DashboardTabFragment.class.getSimpleName();

    private somethingAccountDetails userAccount;
    private somethingContext somethingContext;

//    private ProgressDialog ringProgressDialog;
    private final Handler bkImageChanger = new Handler();
    private final Handler mShowProgress = new Handler();

    private Progress msomethingLogo;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_tab_dashboard, container, false);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        // we must nuke all our threads.
        bkImageChanger.removeCallbacksAndMessages(null);
        mShowProgress.removeCallbacksAndMessages(null);
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        msomethingLogo = (CircularLogoProgress) getActivity().findViewById(R.id.logo);

        // Set tap response
        msomethingLogo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent openActivity = new Intent(view.getContext(), WebViewActivity.class);
                openActivity.putExtra("URL", somethingContext.getFaqUrl());
                startActivity(openActivity);
            }
        });
    }

    @Override
    public void onResume() {
        super.onResume();
    }

    public void loadDisplayData() {
        userAccount = sessionManager.getAccountDetails();
        somethingContext = sessionManager.getUserContextPreference();

        startBkImageLoop();
        showPointsProgressbar();

        // check if we have got a response, and the account isn't null
        if (userAccount != null && userAccount.getAccount() != null) {
            Account account = userAccount.getAccount();
            //SET CUSTOM FONT FOR FIELD LABELS

            // SET DATA
            firstNameField.setText(account.getFirstName());
            firstNameField.setPaintFlags(firstNameField.getPaintFlags() | Paint.UNDERLINE_TEXT_FLAG);
            level.setText(userAccount.getTitle());
        }
        else {
            ApplicationController.getInstance().showCriticalErrorAlert(getActivity(),
                    "Oh no, Critical Error!",

            );
        }
    }

    private void showPointsProgressbar() {
        mShowProgress.postDelayed(new ShowProgressRunnable(userAccount, msomethingLogo), 2000);
        scaleLogoBar();

        msomethingLogo = (Progress) getActivity().findViewById(R.id.logo);

        // Set tap response
/*        msomethingLogo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent openActivity = new Intent(view.getContext(), WebViewActivity.class);
                openActivity.putExtra("URL", ApplicationController.getInstance().somethingModel.faq_url);
                startActivity(openActivity);
            }
        });*/
    }

    private void startBkImageLoop() {
        int mBkImageIndex = 0;
        bkImageChanger.postDelayed(new BkImageRunnable(getActivity(), bkImageChanger, mBkImageIndex), 10000);
    }

    private void scaleLogoBar() {

        final ImageView ivBottomLogo = (ImageView) getActivity().findViewById(R.id.ivBottomLogo);

        ivBottomLogo.post(new Runnable() {

            @Override
            public void run() {

                // logo layout width and height
                int imgW = msomethingLogo.getWidth();
                int imgH = msomethingLogo.getHeight();

                // some more things

            }
        });
    }

    /**
     * We're utilizing an nested inner static classes (ShowProgressRunnable, BkImageRunnable) that uses weak references to the parent classes
     * objects. Previously these were implemented as private functions, with strong references to
     * objects however, if the app is paused or sent to the background or if the activity is destroyed
     * and GC runs leaving our images, and logos locked up from GC.
     */
    private final static class ShowProgressRunnable implements Runnable {
        private final WeakReference<CircularLogoProgress> msomethingLogoRef;
        private final WeakReference<somethingAccountDetails> mUserAccountRef;
        private float mProgress;

        protected ShowProgressRunnable(somethingAccountDetails somethingAccount, Progress somethingLogo) {
            mUserAccountRef = new WeakReference<somethingAccountDetails>(somethingAccount);
            msomethingLogoRef = new WeakReference<CircularLogoProgress>(somethingLogo);
        }


        

    }

    private final static class BkImageRunnable implements Runnable {

        // init null weak references
        private final WeakReference<Handler> mBkImageChangerRef;
        private final WeakReference<Integer> mBkImageIndexRef;
        private final WeakReference<Activity> mActivityRef;

        protected BkImageRunnable(Activity currentActivity, Handler bkImageChanger, int bkImageIndex) {
            mBkImageChangerRef = new WeakReference<Handler>(bkImageChanger);
            mBkImageIndexRef = new WeakReference<Integer>(bkImageIndex);
            mActivityRef = new WeakReference<Activity>(currentActivity);

        }

        @Override
        public void run() {
            somethingContext somethingContext = sessionManager.getUserContextPreference();

            // get our weak ref obj
            int mBkImageIndex = mBkImageIndexRef.get();
            Handler bkImageChanger = mBkImageChangerRef.get();
            final Activity currentActivity = mActivityRef.get();
            ImageView mBackgroundImage = (ImageView) currentActivity.findViewById(R.id.background_image);
            // this is a nuke from orbit option,
            // however we're a static class, and we're anonymous
            // I'm not positive this is the best way, maybe implementing a custom handler also
            // to `handle` this?
            bkImageChanger.removeCallbacksAndMessages(null);
            //mBkImageRunnable_busy = true;
            if (mBkImageIndex >= somethingContext.getAdditionalRedemptionBgs().length) {
                mBkImageIndex = 0;
            }

            Picasso.with(currentActivity)
                    .load(somethingContext.getAdditionalRedemptionBgs()[mBkImageIndex])
                    .noPlaceholder()
                    .into(mBackgroundImage);

            //Log.d(TAG, "Changing background image.");
            ++mBkImageIndex;

            // add another runnable to the queue
            bkImageChanger.postDelayed(new BkImageRunnable(currentActivity, bkImageChanger, mBkImageIndex), 20000);

        }

    }
}


