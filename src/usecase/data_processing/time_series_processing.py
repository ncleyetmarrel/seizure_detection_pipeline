import pandas as pd
import numpy as np

from src.usecase.constants import SeasonalFeature, TempFeaturesOperation, TempFeaturesPeriod


def compute_time_features(dataframe: pd.DataFrame, list_time: list) -> pd.DataFrame:
    """
    This function compute seasoner information from timestamp. These informations
    are used to let know the model weither of seasonality informations is in time series.
    parameters
    ----------
    dataframe: pd.DataFrame
        dataframe constructed from dataset
    list_time: list
        list of time used to compute seasonal information

    return 
    ------
    dataframe: pd.DataFrame
        new dataframe with seasonal informations
    """
    dataframe.timestamp = dataframe.timestamp.apply(convert_timestamp)
    dataframe = dataframe.sort_values(by='timestamp').reset_index(drop=True)

    for time in list_time:
        if time == SeasonalFeature.dayOfWeek.name:
            dataframe[SeasonalFeature.dayOfWeek.name] = dataframe.timestamp.dt.dayofweek
        elif time == SeasonalFeature.month.name:
            dataframe[SeasonalFeature.month.name] = dataframe.timestamp.dt.month
        elif time == SeasonalFeature.hour.name:
            dataframe[SeasonalFeature.hour.name] = dataframe.timestamp.dt.hour
        elif time == SeasonalFeature.minute.name:
            dataframe[SeasonalFeature.minute.name] = dataframe.timestamp.dt.minute
        else:
            dataframe[SeasonalFeature.second.name] = dataframe.timestamp.dt.second

    return dataframe


def compute_contextuals_features(
        dataframe: pd.DataFrame,
        operation: str,
        list_feat: list) -> pd.DataFrame:
    """
    This function will create contextuals features from time domaine features.
    new features will be generated by doing operations like : rolling, diff, etc.
    parameters
    ----------
    dataframe: pd.DataFrame
        dataframe constructed from dataset
    operation: str
        type of operation to use on feature
    list_feat: list
        list of features that we want to use to compute contextuals time domaine features

    return
    ------
    dataframe: pd.DataFrame
        new dataframe with contextuals time domaine features
    """

    dataframe = perform_op_on_features(
        dataframe=dataframe,
        list_feat=list_feat,
        operation=operation)

    return dataframe


def perform_op_on_features(dataframe: pd.DataFrame, list_feat: list, operation: str) -> pd. DataFrame:
    """
    This functioncompute operation on features by iterating over list of features.
    parameters
    ----------
    dataframe: pd.DataFrame
        dataframe from dataset
    list_feat: str
        list of features that we want to use
    operation: str
        operation performed on features : mean, std, etc.
    list_period: list
        list of periods which is used to compute new features

    return
    ------
    dataframe: pd.Dataframe
    """

    [
        create_rolling_variables_given_feature(
            dataframe=dataframe,
            feature=feature,
            operation=operation
        ) for feature in list_feat
    ]

    return dataframe


def create_rolling_variables_given_feature(dataframe: pd.DataFrame, feature: str, operation: str) -> None:

    if operation == TempFeaturesOperation.mean.name:
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p30.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p30.value, min_periods=10).mean()
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p60.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p60.value, min_periods=10).mean()
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p120.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p120.value, min_periods=10).mean()
    elif operation == TempFeaturesOperation.std.name:
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p30.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p30.value, min_periods=10).std()
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p60.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p60.value, min_periods=10).std()
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p120.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p120.value, min_periods=10).std()
    elif operation == TempFeaturesOperation.sum.name:
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p30.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p30.value, min_periods=10).sum()
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p60.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p60.value, min_periods=10).sum()
        dataframe[feature+'_%s' % (TempFeaturesPeriod.p120.name)] = dataframe[feature].rolling(
            window=TempFeaturesPeriod.p120.value, min_periods=10).sum()
    else:
        pass


def diff_operation_from_features(dataframe: pd.DataFrame, list_feat: list) -> pd.DataFrame:
    """
    This function will  compute difference from chosen features. It aims
    to know the variability of features.
    parameters
    ----------
    dataframe: pd.DataFrame
        dataframe constructed from dataset
    list_feat: list
        list of features that we want to use to compute difference operation.

    return
    ------
    dataframe: pd.DataFrame
        new dataframe with variability informations.
    """

    [compute_diff_for_feature(dataframe=dataframe, feature=feat) for feat in list_feat]

    return dataframe


def compute_diff_for_feature(dataframe: pd.DataFrame, feature: str) -> None:
    dataframe[feature+'_diff'] = dataframe[feature].diff().shift(-1)


def convert_timestamp(timestamp):
    return pd.to_datetime(timestamp)
