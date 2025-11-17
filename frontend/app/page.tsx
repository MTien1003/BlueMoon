import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen flex items-center">
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-blue-50 via-slate-50 to-blue-100 -z-10" />
      
      {/* Main container - 2 columns */}
      <div className="w-full max-w-7xl mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-20">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center">
          
          {/* Left Column - Content */}
          <div className="space-y-8">
            {/* Logo and app name */}
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 bg-gradient-to-br from-blue-400 to-teal-500 rounded-xl flex items-center justify-center shadow-lg">
                <span className="text-white font-bold text-2xl">BM</span>
              </div>
              <h1 className="text-3xl font-bold text-slate-800">Blue Moon</h1>
            </div>

            {/* Main heading */}
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-900 leading-tight">
              Quản lý dân cư thông minh với{" "}
              <span className="bg-gradient-to-r from-blue-500 to-teal-500 bg-clip-text text-transparent">
                Blue Moon
              </span>
            </h2>

            {/* Description */}
            <div className="space-y-4 text-slate-600 text-lg leading-relaxed">
              <p>
                Blue Moon là công cụ quản lý dân cư hiện đại, giúp bạn quản lý thông tin cư dân một cách hiệu quả và chuyên nghiệp.
              </p>
              <p>
                Với giao diện trực quan và các tính năng mạnh mẽ, bạn có thể dễ dàng theo dõi, cập nhật và báo cáo thông tin dân cư một cách nhanh chóng.
              </p>
            </div>

            {/* Getting Started button */}
            <Link href="/sign-in" className="px-8 py-4 bg-gradient-to-b from-slate-700 to-slate-900 hover:from-slate-800 hover:to-slate-950 text-white font-semibold rounded-lg transition-all duration-200 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5">
              Getting Started
            </Link>
          </div>

          {/* Right Column - Visual Elements */}
          <div className="relative h-[500px] lg:h-[600px] flex items-center justify-center">
            {/* Decorative background circles */}
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-96 h-96 bg-gradient-to-br from-blue-200/30 to-teal-200/30 rounded-full blur-3xl"></div>
            </div>

            {/* Main visual card - Mockup UI */}
            <div className="relative z-10 w-full max-w-md">
              {/* Floating card 1 - Main */}
              <div className="bg-white rounded-2xl shadow-2xl p-6 transform rotate-3 hover:rotate-0 transition-transform duration-300">
                <div className="space-y-4">
                  <div className="h-4 bg-gradient-to-r from-blue-400 to-teal-400 rounded w-3/4"></div>
                  <div className="space-y-2">
                    <div className="h-3 bg-slate-200 rounded w-full"></div>
                    <div className="h-3 bg-slate-200 rounded w-5/6"></div>
                    <div className="h-3 bg-slate-200 rounded w-4/6"></div>
                  </div>
                  <div className="grid grid-cols-3 gap-2 mt-4">
                    <div className="h-20 bg-gradient-to-br from-blue-100 to-blue-200 rounded-lg"></div>
                    <div className="h-20 bg-gradient-to-br from-teal-100 to-teal-200 rounded-lg"></div>
                    <div className="h-20 bg-gradient-to-br from-slate-100 to-slate-200 rounded-lg"></div>
                  </div>
                </div>
              </div>

              {/* Floating card 2 - Secondary */}
              <div className="absolute -top-8 -right-8 bg-white rounded-xl shadow-xl p-4 transform -rotate-6 hover:rotate-0 transition-transform duration-300 z-20">
                <div className="space-y-2">
                  <div className="h-2 bg-blue-400 rounded w-16"></div>
                  <div className="h-2 bg-slate-200 rounded w-12"></div>
                  <div className="flex gap-2 mt-2">
                    <div className="w-8 h-8 bg-gradient-to-br from-blue-400 to-teal-400 rounded"></div>
                    <div className="w-8 h-8 bg-gradient-to-br from-teal-400 to-blue-400 rounded"></div>
                  </div>
                </div>
              </div>

              {/* Floating card 3 - Tertiary */}
              <div className="absolute -bottom-6 -left-6 bg-white rounded-xl shadow-xl p-4 transform rotate-6 hover:rotate-0 transition-transform duration-300 z-20">
                <div className="space-y-2">
                  <div className="h-3 bg-gradient-to-r from-teal-400 to-blue-400 rounded w-20"></div>
                  <div className="h-2 bg-slate-200 rounded w-16"></div>
                  <div className="h-12 bg-gradient-to-br from-blue-100 to-teal-100 rounded mt-2"></div>
                </div>
              </div>

              {/* Decorative elements */}
              <div className="absolute top-1/4 -left-4 w-16 h-16 bg-blue-400/20 rounded-full blur-xl"></div>
              <div className="absolute bottom-1/4 -right-4 w-20 h-20 bg-teal-400/20 rounded-full blur-xl"></div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
